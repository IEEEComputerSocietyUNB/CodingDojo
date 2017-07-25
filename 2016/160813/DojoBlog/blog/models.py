from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=256, default='')
    text = models.TextField(default='')
    creation_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title