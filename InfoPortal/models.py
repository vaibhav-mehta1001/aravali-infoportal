from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User
# Create your models here.

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)
class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200,unique=True)
    publish = models.BooleanField(default=True)
    modified= models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()
	
    
    def __str__(self):
        return self.title
     
    
class Meta:
    verbose_name = "Blog Entry"
    verbose_name_plural = "Blog Entries"
    ordering = ["-date"]
    

class SagarPost(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length= 20)
    slug = models.SlugField(max_length=200,unique=True)
    publish = models.BooleanField(default=True)
    modified= models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()

	
	
    def __str__(self):
        return self.title
		
class SagarQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)
		
		
class HimgiriPost(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length= 20)
    slug = models.SlugField(max_length=200,unique=True)
    publish = models.BooleanField(default=True)
    modified= models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()

	
	
    def __str__(self):
        return self.title
		
class HimgiriQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)
		
		
		
class VasundharaPost(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length= 20)
    slug = models.SlugField(max_length=200,unique=True)
    publish = models.BooleanField(default=True)
    modified= models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()
	
    def __str__(self):
        return self.title
		
class VasundharaQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)
		
		
class SrishtiPost(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length= 20)
    slug = models.SlugField(max_length=200,unique=True)
    publish = models.BooleanField(default=True)
    modified= models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()

	
	
    def __str__(self):
        return self.title
		
class SrishtiQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class EnvPost(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length= 20)
    slug = models.SlugField(max_length=200,unique=True)
    publish = models.BooleanField(default=True)
    modified= models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()

	
	
    def __str__(self):
        return self.title
		
		
class MunSocQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class MunSocPost(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length= 20)
    slug = models.SlugField(max_length=200,unique=True)
    publish = models.BooleanField(default=True)
    modified= models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()

	
	
    def __str__(self):
        return self.title
		

