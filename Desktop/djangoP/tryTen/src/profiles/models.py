from django.db import models
import random
import os

def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splittext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    new_filename=random.randint(1,345742)
    name,ext = get_filename_ext(filename)
    final_filename ='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "images/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)


# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=120)
    
    description = models.TextField(default='description default value')
    stock=models.CharField(max_length=120,default='0',blank=True,null=True)
    price=models.DecimalField(max_digits=20,default='1',decimal_places=2 )
    image=models.ImageField(upload_to='images/',null=True,blank=True)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name


    
