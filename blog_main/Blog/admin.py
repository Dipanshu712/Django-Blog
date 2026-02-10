from django.contrib import admin
from .models import Blog, Category, Comment


# =========================
# CATEGORY ADMIN
# =========================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


# =========================
# BLOG ADMIN
# =========================
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'author',
        'status',
        'is_featured',
        'created_at'
    )

    list_filter = (
        'status',
        'category',
        'is_featured',
        'created_at'
    )

    search_fields = (
        'title',
        'short_description',
        'content'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    raw_id_fields = ('author',)

    ordering = ('-created_at',)

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'author')
        }),
        ('Content', {
            'fields': ('short_description', 'content', 'featured_image')
        }),
        ('Settings', {
            'fields': ('status', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


# =========================
# COMMENT ADMIN
# =========================
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'blog',
        'parent',
        'is_approved',
        'created_at'
    )

    list_filter = (
        'is_approved',
        'created_at'
    )

    search_fields = (
        'user__username',
        'content',
        'blog__title'
    )

    ordering = ('-created_at',)

    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"

    def disapprove_comments(self, request, queryset):
        queryset.update(is_approved=False)
    disapprove_comments.short_description = "Disapprove selected comments"
