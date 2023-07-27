from django.db import models
from userauth.models import User

class Todo(models.Model):
    todo = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo List'
        
    def __str__(self):
        return self.title

# Create your models here.
