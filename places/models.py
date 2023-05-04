from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self) -> str:
        return self.title
