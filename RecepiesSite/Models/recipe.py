import datetime

from django.contrib.auth.models import User
from django.db import models
from users.models import UserProfile


class Recipe(models.Model):
    choices =[('Worldwide','Worldwide'),
              ('Bulgarian', 'Bulgarian'),
              ('Asian', 'Asian'),
              ('Thai', 'Thai'),
              ('Chinese', 'Chinese'),
              ('Indian', 'Indian'),
              ('Italian', 'Italian'),
    ]
    title = models.CharField(max_length=40)
    image_url = models.ImageField(upload_to='recipes')
    description = models.TextField()
    date = models.DateField(default=datetime.datetime.now, editable=False)
    type = models.CharField(max_length=30, choices=choices, default= 'Bulgarian')
    ingredients = models.TextField()
    time_needed = models.IntegerField()
    author = models.ForeignKey(UserProfile , on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id}; {self.title}; {self.type}'
