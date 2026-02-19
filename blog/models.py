from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )

    # number of likes on the post
    likes = models.PositiveIntegerField(default=0)

    # date and time of post creation
    created_at = models.DateTimeField(auto_now_add = True, null = True)

    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

