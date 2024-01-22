from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Wards(models.Model):
    questioner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="wardss_exhibited"
    )
    name = models.CharField(max_length=30)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    def __str__(self):
        return f"単語名:{self.name},出品者:{self.exhibitor}"
