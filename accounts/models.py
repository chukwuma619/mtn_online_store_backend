from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser


class MyUser(EmailAbstractUser):
    # Custom fields
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    objects = EmailUserManager()
