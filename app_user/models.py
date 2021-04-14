from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    TEACHER = 1
    STUDENT = 2
    PARENT = 3

    ROLE_CHOICES = (
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (PARENT, 'Parent'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=2)

