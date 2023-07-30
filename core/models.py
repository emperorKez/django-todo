from django.db import models
from userauth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=250, blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=False, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo List'
        
    def __str__(self):
        return self.title
