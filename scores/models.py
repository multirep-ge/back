from django.db import models


class Score(models.Model):
    comment = models.CharField(max_length=255, null=True, blank=True, default=None)
    score = models.DecimalField(max_digits=3, decimal_places=2)
    user = models.ForeignKey('users.MyUser', on_delete=models.CASCADE)
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('listing', 'user')

    def __str__(self):
        return f"{self.user.__str__()} -> {self.listing.__str__()} : {self.score}"
