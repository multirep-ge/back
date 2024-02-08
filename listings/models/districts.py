from django.db import models


class District(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey('listings.City', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
