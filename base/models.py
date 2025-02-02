from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# models.py
class task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title  # Changed to return self.title

    class Meta:
        ordering = ['complete']
