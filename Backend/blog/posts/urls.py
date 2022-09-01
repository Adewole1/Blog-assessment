# posts/urls.py

from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (PostCreateView, PostDetailView, 
                    PostListView, MyTokenObtainPairView, 
                    RegisterView)

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_details"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]

# urlpatterns += router.urls