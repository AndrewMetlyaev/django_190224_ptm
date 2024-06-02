from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
