from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=50)
    f_name=models.CharField(max_length=50,default='')
    roll_no=models.IntegerField()

    def __str__(self):
        return f"name={self.name}, roll no={self.roll_no}, f_name={self.f_name}"


class Registration(models.Model):
    firstname=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=50)

    def __str__(self):
        return f"firstname={self.firstname}, last_name={self.last_name}, email={self.email}, password={self.password},address={self.address}"

   
STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(max_length=200, unique=True)
    # author = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='blog_posts')
    author=models.CharField(max_length=40)
    created_on = models.DateTimeField( auto_now_add=True)
    updated_on = models.DateTimeField( auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100,null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}' .format(self.post.title, self.name)