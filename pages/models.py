from django.db import models
from ckeditor.fields import RichTextField
from slugify import slugify
from django.contrib.auth.models import User
from django.db.models import Count
from datetime import datetime
# Create your models here.

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category')
    slug = models.SlugField(null=False,blank=True,db_index=True,editable=False,unique=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    titlePrefix = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE)
    subject = RichTextField()
    viewCounter = models.IntegerField(default=0)
    LastUpdate = models.DateTimeField(default=datetime.now)
    author = models.CharField(max_length=50)
    is_commentable = models.BooleanField(default=True)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Topic.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    message = RichTextField()
    time = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)

class Post(models.Model):
    titlePrefix = models.CharField(max_length=25)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    text = models.TextField()