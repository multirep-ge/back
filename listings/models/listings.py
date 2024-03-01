from django.db import models
from django.utils.timezone import now


class Listing(models.Model):
    CURRENCY_CHOICES = [
        ('GEL', '₾'),
        ('USD', '$'),
    ]
    TIME_UNIT_CHOICES = [
        ('საათში', 'hour'),
        ('გაკვეთილში', 'per_lesson'),
        ('თვეში', 'month'),

    ]
    teacher = models.ForeignKey('users.Teacher', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='GEL')
    subject = models.ForeignKey('listings.Subject', on_delete=models.CASCADE)
    photo = models.ImageField(null=True, upload_to="images/listing")
    views = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(default=now)
    city = models.ForeignKey('listings.City', on_delete=models.CASCADE, null=True)
    district = models.ForeignKey('listings.District', on_delete=models.CASCADE, null=True, blank=True)
    time_unit = models.CharField(max_length=10, choices=TIME_UNIT_CHOICES, default='საათში')

    _score = models.DecimalField(default=0.0, decimal_places=2, max_digits=3)

    def __str__(self):
        return self.title
