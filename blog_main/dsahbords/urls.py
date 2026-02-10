from django.urls import path
from . import views

urlpatterns = [

    # =========================
    # DASHBOARD
    # =========================
    path('', views.dashboard, name='dashboard'),

    # =========================
    # CATEGORY SECTION
    # Admin + Manager + Editor
    # =========================
    path('categories/', views.categories_view, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:id>/', views.delete_category, name='delete_category'),

    # =========================
    # BLOG SECTION
    # Admin + Manager + Editor
    # =========================
    path('blogs/', views.blog_list, name='blogs'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('blogs/edit/<int:id>/', views.edit_blog, name='edit_blog'),
    path('blogs/delete/<int:id>/', views.delete_blog, name='delete_blog'),

    # =========================
    # USER MANAGEMENT
    # Admin + Manager ONLY
    # =========================
    path('users/', views.users_list, name='users_list'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/delete/<int:id>/', views.delete_user, name='delete_user'),
]
