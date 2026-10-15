from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    class Role(models.TextChoices):
        JOB_SEEKER = "JOB_SEEKER", "Job Seeker"
        RECRUITER = "RECRUITER", "Recruiter"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.JOB_SEEKER,
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
