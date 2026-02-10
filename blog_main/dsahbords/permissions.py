def is_admin(user):
    return user.is_authenticated and user.is_superuser


def is_manager(user):
    return user.is_authenticated and user.groups.filter(name__iexact='manager').exists()


def is_editor(user):
    return user.is_authenticated and user.groups.filter(name__iexact='editor').exists()


def can_manage_blog_cat(user):
    return is_admin(user) or is_manager(user) or is_editor(user)


def can_manage_users(user):
    return is_admin(user) or is_manager(user)
