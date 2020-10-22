from django.db import models

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

 