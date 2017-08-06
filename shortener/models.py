from django.db import models

#Create your models here.
class KirrURL(models.Model):
    url         = models.CharField(max_length=220,)
    shortcode   = models.CharField(max_length=15, unique=True)
    updated     = models.DateTimeField(auto_now = True) #everytime the model is saved
    timestamp   = models.DateTimeField(auto_now=True) #when model was created
    #mpty_datetime = models.DateTimeFuled ( auto_now= False, auto_now_add = False)
    #shortcode = models.CharField(max_length=15, null=True,blank = False) #empty in db is okay
    #shortcode = models.CharField(max_length=15,default='carlodefault')


    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)


'''
python manage.py makemigrations
python manage.py migrate


'''