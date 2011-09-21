from django.db import models
import urllib2
#from PIL import Image

class TaroCard(models.Model):
    name = models.CharField(max_length=40)
    details = models.TextField(max_length=3000)
    small_icon_url = models.IntegerField('The url small icon')
    big_icon_url  = models.IntegerField('Big icon url number')
    def __unicode__(self):
        return self.name
	
class TaroOrder(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    icon_url = models.CharField('The url icon', max_length=40)
    order = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.name