from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Comment(models.Model):
    """
    Model class for creating a comment to a news story
    """
    comment_body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    story_id = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


    def __str__(self):
        """
        return string representation of the comment
        model class
        """
        return self.comment_body

