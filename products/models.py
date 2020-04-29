from django.db import models
import random
import os

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
class ProductManager(models.Manager):

    def featured(self):
        return self.get_queryset().filter(featured=True)



class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    #image = models.ImageField(upload_to="Folder name", null=True, blank=True)  ** When We Can not Use Custom image Name
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return self.title
    

    #Use For Python 2 Specially
    def __unicode__(self):
        return self.title


