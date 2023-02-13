from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=255)
    visualizations = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=30)
    videos = models.ManyToManyField(Video, related_name="categories")

    def __str__(self) -> str:
        return self.title