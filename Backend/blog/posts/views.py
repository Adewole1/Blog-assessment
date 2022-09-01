# posts/views

from rest_framework import generics, filters

from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer
from .models import BlogPost
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostCreateSerializer    


class PostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'author']
    ordering = ['-created_at']


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogPost.objects.all()
    serializer_class = PostDetailSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = BlogPost.objects.all()
#     serializer_class = PostSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer