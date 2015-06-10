from django.db import models

# Create your models here.
class PortfolioCreation(models.Model):
    name = models.CharField(blank=True, max_length=250)
    title = models.CharField(unique=True,blank=True, max_length=250)
    date_created = models.DateTimeField(null=True, auto_now_add=True)
    notes = models.TextField(blank=True)
    media = models.ImageField()

     def __unicode__(self):
        return self.name
