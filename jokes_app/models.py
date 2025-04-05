from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Joke(models.Model):
    content = models.TextField(
        validators=[
            MinLengthValidator(10, message="Joke content must be at least 10 characters long."),
            MaxLengthValidator(500, message="Joke content cannot exceed 500 characters.")
        ]
    )
    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, message="Author name must be at least 2 characters long."),
            MaxLengthValidator(100, message="Author name cannot exceed 100 characters.")
        ]
    )
    category = models.CharField(max_length=50, default="general")
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f"{self.author}: {self.content[:50]}..."

    @classmethod
    def random(cls):
        """Return a random joke from the database."""
        return cls.objects.order_by('?').first()