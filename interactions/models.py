from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="interaction_likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "project")
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return f"{self.user.username} likes {self.project.title}"
