from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    #def __unicode__(self): #For Python 2, use __str__ on Python 3
    def __str__(self):
        return self.name
    
    #give models matadata using the Meta class
    class Meta:
        verbose_name_plural = "Categories"
    
    
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title