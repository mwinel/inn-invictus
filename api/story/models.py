from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Story(models.Model):
    """
    Model class for creating a news story
    """
    story_title = models.CharField(max_length=120)
    created_on = models.DateTimeField(default=timezone.now)
    story_body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


    def __str__(self):
        """
        return string representation of the story
        model class
        """
        return self.story_title


