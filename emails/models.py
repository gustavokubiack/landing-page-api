from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"
