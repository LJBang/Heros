from django.db import models
from accounts.models import User

# Create your models here.
class Article(models.Model):
    menuid      = models.CharField(max_length=120,default='')
    author      = models.CharField(max_length=120)
    title       = models.CharField(max_length=120)
    text        = models.TextField()
    place       = models.CharField(max_length=120)
    price       = models.CharField(max_length=120,default = '')
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title