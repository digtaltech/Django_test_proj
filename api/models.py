import uuid
from django.db import models

# Create your models here.
class Data(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    fio = models.TextField(max_length=100)
    balance = models.IntegerField()
    hold = models.IntegerField()
    status = models.BooleanField(default=1)
