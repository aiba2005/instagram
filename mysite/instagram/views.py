from rest_framework import viewsets, generics, status
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *
from  rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(username=self.request.user.username)



class UserProfileAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(username=self.request.user.username)

class UserProfileEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileEditSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer


class UserPostDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserPostDetailSerializer


class PostLikeCreateAPIView(generics.CreateAPIView):
    serializer_class = PostLikeCreateSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer


class CommentLikeCreateView(generics.CreateAPIView):
    serializer_class = CommentLikeSerializer


class StoryCreateAPIView(generics.CreateAPIView):
    serializer_class = StoryCreateSerializer


class StoryListAPIView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSerializer

class StoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = UserPostDetailSerializer



class SaveViewSet(viewsets.ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer


class SaveItemViewSet(viewsets.ModelViewSet):
    queryset = SaveItem.objects.all()
    serializer_class = SaveItemSerializer

