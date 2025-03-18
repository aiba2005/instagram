from django.urls import path, include
from .views import *
from  rest_framework import routers


router = routers.SimpleRouter()
router.register(r'saves', SaveViewSet, basename='saves_list')
router.register(r'save_items', SaveItemViewSet, basename='save_items_list')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('user/', UserProfileAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileEditAPIView.as_view(), name='user_edit'),

    path('post/', PostListAPIView.as_view(), name='post_list'),
    path('post/<int:pk>/', UserPostDetailAPIView.as_view(), name='post_detail'),
    path('post/create', PostCreateAPIView.as_view(), name='post_create'),
    path('post_like/create', PostLikeCreateAPIView.as_view(), name='post_like_create'),

    path('story/', StoryListAPIView.as_view(), name='story_list'),
    path('story/<int:pk>/', StoryDetailAPIView.as_view(), name='story_detail'),
    path('post/create', StoryCreateAPIView.as_view(), name='post_create'),

    path('comment/create', CommentCreateAPIView.as_view(), name='comment_create'),
    path('comment_like/create', CommentLikeCreateView.as_view(), name='comment_like_create'),

]
