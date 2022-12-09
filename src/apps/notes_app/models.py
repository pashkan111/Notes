from django.db import models
import uuid
from apps.users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
        

class Note(models.Model):
    guid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
        )

    def __str__(self) -> str:
        return self.name