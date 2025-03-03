from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    status = models.IntegerField()
        
class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    heading = models.CharField(max_length=500)
    description = RichTextField(null=True,blank=True)
    image = models.ImageField(upload_to="post_images",default="",null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField()
        
class Post_views(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=None)

class User(models.Model):
    user = models.CharField(max_length=200,default=None)

class Post_like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    status = models.IntegerField(default=1)