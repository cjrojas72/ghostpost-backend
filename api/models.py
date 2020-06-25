from django.db import models
from django.utils import timezone


class Post(models.Model):
    CHOICES = [
        ("BO", "BOAST"),
        ("RO", "ROAST")
    ]

    post_id = models.CharField(max_length=6)
    choice = models.CharField(
        max_length=2,
        choices=CHOICES,
        default="BO"
    )
    body = models.TextField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_id
