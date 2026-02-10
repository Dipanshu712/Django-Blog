from django.shortcuts import get_object_or_404, redirect, render
from Blog.models import Blog, Category
from django.http import HttpResponse

from assignments.models import About, SocialLink
from django.db.models import Q


def home(request):

    featured_posts = Blog.objects.filter(
        is_featured=True,
        status=Blog.Status.PUBLISHED
    ).order_by("-updated_at")

    posts = Blog.objects.filter(
        is_featured=False,
        status=Blog.Status.PUBLISHED
    ).order_by("-updated_at")

    about = About.objects.first()
    social_links = SocialLink.objects.all()
    print("SOCIAL LINKS:", social_links)

    context = {
        "featured_posts": featured_posts,
        "posts": posts,
        "about": about,
        "social_links": social_links,
    }

    return render(request, "home.html", context)



# def posts_by_category(request,category_id):
#     # Fetech the posts that belongs to the category with the id category_id
#     posts = Blog.objects.filter(status=Blog.Status.PUBLISHED,category=category_id)
#     context = {
#         'posts':posts,
#     }
#     return HttpResponse(request,'posts_by_category.html',context)
# # Context = Python data → HTML template


from django.shortcuts import render, redirect
from Blog.models import Blog, Category

def posts_by_category(request, category_id):
    # 1️⃣ Try to get the category using category_id
    # If category does not exist, redirect to home page
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except Category.DoesNotExist:
    #     return redirect('home')
    category = get_object_or_404(Category, pk=category_id)


    # 2️⃣ Get all PUBLISHED blog posts of this category
    posts = Blog.objects.filter(
        category=category,                 # correct: category is now defined
        status=Blog.Status.PUBLISHED       # only published posts
    )

    # 3️⃣ Send data to template using context
    context = {
        "category": category,   # category object
        "posts": posts          # list of blog posts
    }

    # 4️⃣ Render HTML page with data
    return render(request, "posts_by_category.html", context)



def blog_detail(request, slug):
    post = get_object_or_404(
        Blog,
        slug=slug,
        status=Blog.Status.PUBLISHED
    )

    comments = post.comments.filter(
        is_approved=True,
        parent__isnull=True
    )

    can_manage_comments = (
        request.user.is_authenticated and (
            request.user.is_superuser or
            request.user.groups.filter(name__iexact='manager').exists()
        )
    )

    return render(request, 'blogs.html', {
        'post': post,
        'comments': comments,
        'can_manage_comments': can_manage_comments
    })






from django.shortcuts import render
from django.db.models import Q
from .models import Blog

def Search(request):
    query = request.GET.get('q')   # ✅ MATCH FORM

    blogs = Blog.objects.filter(status=Blog.Status.PUBLISHED)

    if query and query.strip():    # ✅ THIS CHECK IS IMPORTANT
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(short_description__icontains=query)
        )

    return render(request, 'search.html', {
        'blogs': blogs,
        'keyword': query
    })


# def register(request):
#     return render(request,'register.html')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            messages.success(request, "Account created successfully 🎉")
            return redirect("login")  # change to your home url


    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")




from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)          # clears session
    return redirect('login') # redirect after logout


# Comments section 
# =====================
# COMMENTS PERMISSIONS
# =====================
def can_delete_comment(user, comment):
    return (
        user.is_superuser or
        user.groups.filter(name__iexact='manager').exists() or
        comment.user == user
    )


# =====================
# ADD COMMENT
# =====================
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog, Comment


@login_required
def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        Comment.objects.create(
            blog=blog,
            user=request.user,
            content=request.POST.get('content'),
            parent_id=request.POST.get('parent') or None
        )
        messages.success(request, 'Comment added successfully')

    return redirect('blog_detail', slug=blog.slug)


# =====================
# DELETE COMMENT
# =====================
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if not can_delete_comment(request.user, comment):
        messages.error(request, 'Permission denied')
        return redirect('blog_detail', slug=comment.blog.slug)

    comment.delete()
    messages.success(request, 'Comment deleted successfully')

    return redirect('blog_detail', slug=comment.blog.slug)
