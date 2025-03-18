from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from jinja2.runtime import markup_join
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(65)], null=True, blank=True)
    bio = models.TextField( null=True, blank=True)
    image = models.ImageField(upload_to='user_images/',  null=True, blank=True)
    website = models.URLField( null=True, blank=True)

    def get_count_following(self):
        people = self.user_following.all()
        if people.exists():
            return people.count()
        return 0


    def get_count_follower(self):
        people = self.user_follower.all()
        if people.exists():
            return people.count()
        return 0

    def get_count_post(self):
        people = self.post.all()
        if people.exists():
            return people.count()
        return 0

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.username}'






class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_follower', null=True, blank=True)
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_following', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def clean(self):
        super().clean()
        if not self.follower and not self.following :
            raise ValidationError('Choose minimum one of (follower, following)!')


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    video = models.FileField(upload_to='post_videos/', null=True, blank=True)
    description = models.TextField()
    hashtag = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def clean(self):
        super().clean()
        if not self.image and not self.video :
            raise ValidationError('Choose minimum one of (video, image)!')


    def get_count_post_like(self):
        people = self.post_like.all()
        if people.exists():
            return people.count()
        return 0


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_count_comment_like(self):
        people = self.comment_like.all()
        if people.exists():
            return people.count()
        return 0



class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_like')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment')

class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_images/', null=True, blank=True)
    video = models.FileField(upload_to='story_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if not self.image and not self.video :
            raise ValidationError('Choose minimum one of (video, image)!')




class Save(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class SaveItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    save = models.ForeignKey(Save, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    people = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to= 'message_images/', null=True, blank=True)
    video = models.FileField(upload_to='message_videos/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

# filter(hashtag), search(username), order(post(created_at))
# permission
# jwt