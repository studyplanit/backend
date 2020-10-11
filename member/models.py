from django.db import models


class Member(models.Model):
    nickname=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    mail=models.CharField(max_length=50)
    point=models.IntegerField(default=0)

    class Meta:
        db_table='member'