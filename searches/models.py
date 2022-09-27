from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Search(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("search_detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    search = models.ForeignKey(Search, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    avatar_url = models.TextField()
    html_url = models.TextField()
    url = models.TextField()
    repos_url = models.TextField()
    skills = models.TextField()
    star = models.BooleanField(default=False)
    got_skills = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Comment(models.Model):  # new
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
