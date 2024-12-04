from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    PRIORITY_CHOICES = [
       (LOW, 'Low'),
       (MEDIUM, 'Medium'),
       (HIGH, 'High'),
    ]

    tittle = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default=MEDIUM)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
       return self.tittle
    

class Category(models.Model):
    name = models.CharField(max_length=100)    

    def _str_(self):
       return self.name  

class TaskCategory(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)