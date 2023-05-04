from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
