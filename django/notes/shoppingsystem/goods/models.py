from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=10)

    def __unicode__(self):
        return u'Category:%s' %self.cname
