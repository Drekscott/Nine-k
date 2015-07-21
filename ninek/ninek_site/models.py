from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class About(models.Model):

    about_name = models.CharField(max_length=120)
    about_me = models.TextField(max_length=None)
    about_pic = models.ImageField(upload_to=None)

    def __unicode__(self):
        return self.about_name
class Category(models.Model):

    name = models.CharField(max_length=120)
    views = models.IntegerField(default=0)
    slug = models.AutoSlugField(populate_from='name')

    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Page(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=120)
    author_name = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)
    upload_image = models.ImageField(upload_to=None)
    page_content = models.TextField(max_length=None)

    def __unicode__(self):
        return self.title
