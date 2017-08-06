
from django.db import models 
from .utils import code_generator, create_shortcode

#Create your models here.

class KirrURLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_main = super(KirrURLManager, self).all(*args,**kwargs)
        qs = qs_main.filter(active=True)
        return qs
    
    def refresh_shortcodes(self):
        qs = KirrURL.objects.filter(id__gte=1)
        new_codes = 0 
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)






class KirrURL(models.Model):
    url         = models.CharField(max_length=220,)
    shortcode   = models.CharField(max_length=15, unique=True, blank= True)
    updated     = models.DateTimeField(auto_now = True) #everytime the model is saved
    timestamp   = models.DateTimeField(auto_now=True) #when model was created
    active      = models.BooleanField(default=True)

    objects = KirrURLManager()

    #mpty_datetime = models.DateTimeFuled ( auto_now= False, auto_now_add = False)
    #shortcode = models.CharField(max_length=15, null=True,blank = False) #empty in db is okay
    #shortcode = models.CharField(max_length=15,default='carlodefault')

    def save(self, *args, **kwargs):
        if  not self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
            super(KirrURL,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
    

'''
python manage.py makemigrations
python manage.py migrate

'''