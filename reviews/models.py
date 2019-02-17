from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def email(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('writer-detail', args=[str(self.user.id)])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=10000)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now=True)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=1000)
    parent = models.ForeignKey('Comment', null=True, on_delete=models.CASCADE)
