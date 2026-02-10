


from .models import Category
from assignments.models import SocialLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories)


# A context processor is a function that sends data to ALL templates automatically.
def get_social_link(request):
    social_links = SocialLink.objects.all()
    return dict(social_links = social_links)




def user_role(request):
    if request.user.is_authenticated:
        return {
            'is_manager': request.user.groups.filter(name='Manager').exists()
        }
    return {}





from dsahbords.permissions import can_manage_blog_cat, can_manage_users

def dashboard_permissions(request):
    if request.user.is_authenticated:
        return {
            'can_manage_blog_cat': can_manage_blog_cat(request.user),
            'can_manage_users': can_manage_users(request.user),
        }
    return {}
