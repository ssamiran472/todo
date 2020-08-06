from django.db import models


class Todo(models.Model):
    title       = models.CharField(max_length=100, default='')
    description = models.CharField(max_length =300, default='')
    completed   = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class Blogs(models.Model):
    title=models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length =300)
    created_at  = models.DateTimeField(auto_now_add=True)