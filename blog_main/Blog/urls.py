from django.urls import include, path
from . import views
from Blog import views as BlogsViews

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('blogs/search/', BlogsViews.Search, name='search'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),   # ✅ ADD THIS
    path('logout/',views.logout_view,name='logout'),
    # Dashboards
    path('dashboard/',include('dsahbords.urls')),
    # Comments 
    path('blog/<int:blog_id>/comment/',views.add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]
