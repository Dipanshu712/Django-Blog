from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User, Group

from Blog.models import Blog, Category


# ======================================================
# 🔐 PERMISSION HELPERS (SINGLE SOURCE OF TRUTH)
# ======================================================
from django.contrib.auth.models import Group

def can_manage_blog_cat(user):
    """
    Admin, Manager, Editor → Blogs & Categories
    """
    return (
        user.is_authenticated and (
            user.is_superuser or
            user.groups.filter(name__in=['Manager', 'Editor']).exists()
        )
    )


def can_manage_users(user):
    """
    Admin & Manager → Users
    """
    return (
        user.is_authenticated and (
            user.is_superuser or
            user.groups.filter(name='Manager').exists()
        )
    )



# ======================================================
# 📊 DASHBOARD
# ======================================================

@login_required(login_url='login')
def dashboard(request):
    can_blog_cat = can_manage_blog_cat(request.user)
    can_users = can_manage_users(request.user)

    context = {
        'total_blogs': Blog.objects.count(),
        'total_categories': Category.objects.count(),

        # 🔑 THESE TWO LINES WERE MISSING
        'can_manage_blog_cat': can_blog_cat,
        'can_manage_users': can_users,
    }

    if can_users:
        context['total_users'] = User.objects.count()

    return render(request, 'dashboard/dashboard.html', context)



# ======================================================
# 📂 CATEGORY SECTION
# ======================================================

@login_required(login_url='login')
def categories_view(request):
    return render(request, 'dashboard/categories.html', {
        'categories': Category.objects.all().order_by('-id'),
        'can_manage_blog_cat': can_manage_blog_cat(request.user),
    })


@login_required(login_url='login')
@user_passes_test(can_manage_blog_cat)
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if not name:
            messages.error(request, 'Category name is required')
        else:
            Category.objects.create(name=name)
            messages.success(request, 'Category added successfully')
            return redirect('categories')

    return render(request, 'dashboard/add_category.html')


@login_required(login_url='login')
@user_passes_test(can_manage_blog_cat)
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        name = request.POST.get('name')

        if not name:
            messages.error(request, 'Category name is required')
        else:
            category.name = name
            category.save()
            messages.success(request, 'Category updated successfully')
            return redirect('categories')

    return render(request, 'dashboard/edit_category.html', {'category': category})


@login_required(login_url='login')
@user_passes_test(can_manage_blog_cat)
def delete_category(request, id):
    if request.method == 'POST':
        get_object_or_404(Category, id=id).delete()
        messages.success(request, 'Category deleted successfully')

    return redirect('categories')


# ======================================================
# 📝 BLOG SECTION
# ======================================================

@login_required(login_url='login')
def blog_list(request):
    blogs = Blog.objects.select_related('category', 'author').order_by('-id')

    return render(request, 'dashboard/blogs.html', {
        'blogs': blogs,
        'can_manage_blog_cat': can_manage_blog_cat(request.user),
    })


@login_required(login_url='login')
@user_passes_test(can_manage_blog_cat)
def add_blog(request):
    categories = Category.objects.all()

    # Editor → only himself as author
    if request.user.groups.filter(name__iexact='editor').exists():
        users = User.objects.filter(id=request.user.id)
    else:
        users = User.objects.all()

    if request.method == 'POST':
        Blog.objects.create(
            title=request.POST.get('title'),
            category_id=request.POST.get('category'),
            author_id=request.POST.get('author'),
            short_description=request.POST.get('short_description'),
            content=request.POST.get('content'),
            status=int(request.POST.get('status', 0)),
            is_featured=True if request.POST.get('is_featured') else False,
            featured_image=request.FILES.get('featured_image')
        )
        messages.success(request, 'Blog added successfully')
        return redirect('blogs')

    return render(request, 'dashboard/add_blog.html', {
        'categories': categories,
        'users': users,
    })


@login_required(login_url='login')
@user_passes_test(can_manage_blog_cat)
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    # Editor can edit ONLY own blog
    if (
        request.user.groups.filter(name__iexact='editor').exists() and
        blog.author != request.user
    ):
        messages.error(request, 'You can edit only your own blog')
        return redirect('blogs')

    categories = Category.objects.all()
    users = User.objects.all()

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.category_id = request.POST.get('category')
        blog.author_id = request.POST.get('author')
        blog.short_description = request.POST.get('short_description')
        blog.content = request.POST.get('content')
        blog.status = int(request.POST.get('status', blog.status))
        blog.is_featured = True if request.POST.get('is_featured') else False

        if request.FILES.get('featured_image'):
            blog.featured_image = request.FILES.get('featured_image')

        blog.save()
        messages.success(request, 'Blog updated successfully')
        return redirect('blogs')

    return render(request, 'dashboard/edit_blog.html', {
        'blog': blog,
        'categories': categories,
        'users': users,
    })


@login_required(login_url='login')
@user_passes_test(can_manage_blog_cat)
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    # Editor can delete ONLY own blog
    if (
        request.user.groups.filter(name__iexact='editor').exists() and
        blog.author != request.user
    ):
        messages.error(request, 'You can delete only your own blog')
        return redirect('blogs')

    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog deleted successfully')

    return redirect('blogs')


# ======================================================
# 👥 USER MANAGEMENT (ADMIN + MANAGER)
# ======================================================

@login_required(login_url='login')
@user_passes_test(can_manage_users)
def users_list(request):
    users = User.objects.prefetch_related('groups').order_by('-date_joined')

    data = []
    for u in users:
        if u.is_superuser:
            role = 'admin'
        elif u.groups.filter(name__iexact='manager').exists():
            role = 'manager'
        elif u.groups.filter(name__iexact='editor').exists():
            role = 'editor'
        else:
            role = 'user'

        data.append({
            'id': u.id,
            'username': u.username,
            'date_joined': u.date_joined,
            'is_superuser': u.is_superuser,
            'role': role,
        })

    return render(request, 'dashboard/users.html', {
        'users': data,
        'can_manage_users': True,
    })


@login_required(login_url='login')
@user_passes_test(can_manage_users)
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('add_user')

        user = User.objects.create_user(username=username, password=password)

        if role == 'manager':
            user.groups.add(Group.objects.get(name__iexact='manager'))
        elif role == 'editor':
            user.groups.add(Group.objects.get(name__iexact='editor'))

        messages.success(request, 'User created successfully')
        return redirect('users_list')

    return render(request, 'dashboard/add_user.html')


@login_required(login_url='login')
@user_passes_test(can_manage_users)
def delete_user(request, id):
    user = get_object_or_404(User, id=id)

    if user.is_superuser:
        messages.error(request, 'Cannot delete admin user')
        return redirect('users_list')

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully')

    return redirect('users_list')

# 8.24