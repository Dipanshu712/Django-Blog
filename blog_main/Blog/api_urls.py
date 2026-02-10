from django.urls import path
from .api_views import *

urlpatterns = [
    path("blogs/", BlogListAPI.as_view()),
    path("blogs/<slug:slug>/", BlogDetailAPI.as_view()),
    path("categories/", CategoryListAPI.as_view()),
    path("categories/<int:category_id>/blogs/", BlogsByCategoryAPI.as_view()),
    path("comments/", CommentCreateAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("register/", RegisterAPI.as_view()),
]
