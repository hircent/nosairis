from django.db import models

# Create your models here.

class Terminals(models.Model):
  switch = models.CharField(max_length=20)
  t1 = models.IntegerField()
  t2 = models.IntegerField()
  t3 = models.IntegerField()
  t4 = models.IntegerField()
  t5 = models.IntegerField()
  ts = models.IntegerField()