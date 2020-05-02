from django.db import models
from products.models import Product

#When We want To auto Generating Slag
from django.db.models.signals import pre_save, post_save
from products.utills import unique_slug_generator

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)


def __str__(self):
    return self.title

def __unicode__(self):
    return self.title



#Auto Genarateing Slug Function
def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Tag)

