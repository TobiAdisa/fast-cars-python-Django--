from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Users(AbstractUser):
    # id = models.AutoField(primary_key=True)
    profile_image = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'users'
        managed = True

    def _str_(self):
        return self.username