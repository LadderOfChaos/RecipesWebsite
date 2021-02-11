from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    profile_picture = models.ImageField(default='default.jpg', upload_to='users', )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


