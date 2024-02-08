from django.db import models
from django.utils.timezone import now

from listings.models.listings import Listing
from users.models import MyUser


class Favorite(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=now)

    class Meta:
        unique_together = ('listing', 'user')

    def __str__(self):
        return f"{self.user} ({self.user.email}) has favorited {self.listing} ({self.listing.title})"
