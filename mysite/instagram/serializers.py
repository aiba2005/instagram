from rest_framework import serializers
from .models import UserProfile, Follow, Post, PostLike, Comment, CommentLike, Story, Save, SaveItem
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'bio', 'image', 'website')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'





class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentPostSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    get_count_comment_like = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = Comment
        fields = ['user', 'text', 'parent', 'get_count_comment_like', 'created_at' ]

    def get_count_comment_like(self, obj):
        return obj.get_count_people()


class PostListSerializer(serializers.ModelSerializer):
    post_comment = CommentPostSerializer(many=True, read_only=True)
    count_post_like = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    user = UserProfileSimpleSerializer()
    class Meta:
        model = Post
        fields = ['id', 'user', 'image', 'video', 'description', 'hashtag', 'count_post_like', 'created_at', 'post_comment']

    def get_count_post_like(self, obj):
        return obj.get_count_post_like()


class PostUserSerializer(serializers.ModelSerializer):
    post_comment = CommentPostSerializer(many=True, read_only=True)
    count_post_like = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = Post
        fields = ['image', 'video', 'description', 'hashtag', 'count_post_like', 'created_at', 'post_comment']


    def get_count_post_like(self, obj):
        return obj.get_count_post_like()

class PostLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'



class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'


class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class StoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'image', 'video', 'created_at']


class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'


class SaveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveItem
        fields = '__all__'



class UserProfileListSerializer(serializers.ModelSerializer):
    post = PostUserSerializer(many=True, read_only=True)
    count_follower = serializers.SerializerMethodField()
    count_following = serializers.SerializerMethodField()
    count_post = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'last_name', 'image', 'bio', 'website', 'count_following',
                  'count_follower', 'count_post', 'post']

    def get_count_post(self, obj):
        return obj.get_count_post()


    def get_count_following(self, obj):
        return obj.get_count_following()

    def get_count_follower(self, obj):
        return obj.get_count_follower()


class UserPostDetailSerializer(serializers.ModelSerializer):
    post = PostUserSerializer(many=True, read_only=True)
    count_follower = serializers.SerializerMethodField()
    count_following = serializers.SerializerMethodField()
    count_post = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ['username', 'last_name', 'image', 'bio', 'website', 'count_following',
                  'count_follower', 'count_post', 'post']

    def get_count_post(self, obj):
        return obj.get_count_post()


    def get_count_following(self, obj):
        return obj.get_count_following()

    def get_count_follower(self, obj):
        return obj.get_count_follower()