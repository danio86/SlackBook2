from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager

STATUS = ((0, 'Draft'), (1, 'Published'))


# User Model expands the default User Model
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    biography = models.TextField(null=True)
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    loggedin = models.BooleanField(default=True, blank=True)
    online = models.BooleanField(default=False, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


# Topic/Category
class Topic(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


# Channel Model
class Channel(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    guests = models.ManyToManyField(User, related_name='guests', blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    keywords = models.TextField(blank=True)
    private = models.BooleanField(default=False, blank=True)
    permission = models.TextField(blank=True)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


# Chat Model
class Chat(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, max_length=200, default=' ', null=True)
    image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


# Post Model is connected to Channel and Chat
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True,
                                related_name='channel_post')
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)
    image_description = models.TextField(null=True, max_length=200, blank=True)
    keywords = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['-updated_on', '-created_on']

    def __str__(self):
        return self.body[0:30]
