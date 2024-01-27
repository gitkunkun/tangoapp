from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Words(models.Model):
    questioner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="words_questioned"
    )
    name = models.CharField(max_length=30)
    yaku = models.CharField(max_length=30, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, related_name="words"
    )
    ex_1 = models.CharField(max_length=50, null=True)
    ex_1_yaku = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"単語名:{self.name},出題者:{self.questioner}"

class Misstake(models.Model):
    misstake = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="misstaker"
    ),
    miss_word = models.ForeignKey(
        Words, on_delete=models.CASCADE, related_name="missword"
    )