from django.db import models
from datetime import datetime
# Create your models here.


class Group(models.Model):
    group_name = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.group_name)

class Language(models.Model):
    name = models.CharField(max_length=64)
    paradigms = models.CharField(max_length=64, default="")
    group = models.OneToOneField(Group,on_delete=models.CASCADE,null=True,blank=True)
    taken = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)


