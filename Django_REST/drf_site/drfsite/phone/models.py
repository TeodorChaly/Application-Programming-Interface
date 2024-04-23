from django.db import models

class Phones(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title
