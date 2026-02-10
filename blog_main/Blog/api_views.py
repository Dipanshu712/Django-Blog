from rest_framework import generics, permissions
from .models import Blog, Category, Comment
from .serializers import BlogSerializer, CategorySerializer, CommentSerializer

class BlogListAPI(generics.ListAPIView):
    queryset = Blog.objects.filter(status=Blog.Status.PUBLISHED)
    serializer_class = BlogSerializer


class BlogDetailAPI(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(status=Blog.Status.PUBLISHED)
    serializer_class = BlogSerializer
    lookup_field = "slug"


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogsByCategoryAPI(generics.ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(
            category_id=self.kwargs["category_id"],
            status=Blog.Status.PUBLISHED
        )
from rest_framework import generics, permissions
from .serializers import CommentSerializer
from .models import Comment

class CommentCreateAPI(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.contrib.auth.models import User

class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])

        return Response({
            "token": token.key,
            "user_id": token.user_id,
            "username": token.user.username
        })


class RegisterAPI(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = User.objects.create_user(
            username=request.data.get("username"),
            password=request.data.get("password")
        )
        token = Token.objects.create(user=user)

        return Response({
            "token": token.key,
            "username": user.username
        }, status=status.HTTP_201_CREATED)
