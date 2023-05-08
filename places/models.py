from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = HTMLField()
    description_long = HTMLField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    order = models.PositiveSmallIntegerField()
    image = models.ImageField()
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE)

    class Meta:
        ordering = [
            "order",
        ]

    def __str__(self) -> str:
        return f"{self.place.title} ({self.image.url})"
