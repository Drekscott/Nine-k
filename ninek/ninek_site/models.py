from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class About(models.Model):

    about_name = models.CharField(max_length=120)
    about_me = models.TextField(max_length=None)
    about_pic = models.ImageField(upload_to='ninek_site')

    def __unicode__(self):
        return self.about_name
class Category(models.Model):

    name = models.CharField(max_length=120)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def latest_post(self):
        page = self.page_set.order_by('-date_created')
        if page:
            return page[0]
        return None

class Page(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=120)
    author_name = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    upload_image = models.ImageField(upload_to='ninek_site')
    page_content = models.TextField(max_length=None)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title
