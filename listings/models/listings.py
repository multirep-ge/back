from django.db import models
from django.utils.timezone import now

from scores.models import Score


class Listing(models.Model):
    teacher = models.ForeignKey('users.Teacher', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    subject = models.ForeignKey('listings.Subject', on_delete=models.CASCADE)
    photo = models.ImageField(null=True, upload_to="images/listing")
    views = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(default=now)
    currency = models.ForeignKey('listings.Currency', on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey('listings.City', on_delete=models.CASCADE, null=True)
    district = models.ForeignKey('listings.District', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def average_listing_score(self):
        scores = Score.objects.filter(listing=self)
        if scores.exists():
            total_score = sum(score.score for score in scores)
            count = scores.count()
            return total_score / count
        else:
            return 0

    def __str__(self):
        return self.title
