from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    # fields for the business table
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    averagerating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Review(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)
    def __str__(self):
        return self.user.username