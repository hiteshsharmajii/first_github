from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import django.utils.timezone as dut
# Create your models here.

class User(models.Model):
    id = models.CharField(primary_key = True,max_length = 180, blank = False)
    first_name = models.CharField(max_length = 180 ,blank = True)
    last_name = models.CharField(max_length = 180 , blank = True)
    email = models.CharField(max_length = 180 , blank = False)
    password = models.CharField(max_length = 180 , blank = True)
    created_at = models.DateTimeField(default = dut.now(),blank = True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.id