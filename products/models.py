from django.db import models
import random
import os


#When We want To auto Generating Slag
from django.db.models.signals import pre_save, post_save
from .utills import unique_slug_generator

# Create your models here.


#----------------------- If we want Formate image Name than Use This Code -----------------------------#
def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    #print(instance)
    #print(filename)
    new_filename = random.randint(1,956325566)
    name, ext = get_file_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return "products/{new_filename}/{final_filename}".format(new_filename = new_filename, final_filename = final_filename)

#----------------------- If we Use Formate image Name than Use This Code ** End -----------------------------#

#Custom Function For Retrive Data
class ProductManager(models.Manager):

    def featured(self):
        return self.get_queryset().filter(featured=True)


#Database Table Migration Section

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    #image = models.ImageField(upload_to="Folder name", null=True, blank=True)  ** When We Can not Use Custom image Name
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    #Use When we create Custome Function manage (e.g: ProductManager)
    objects = ProductManager()

    def __str__(self):
        return self.title
    

    #Use For Python 2 Specially
    def __unicode__(self):
        return self.title

#Auto Genarateing Slug Function
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)


