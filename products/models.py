from django.db import models
#from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Category(models.Model):

    parent=models.ForeignKey('self',verbose_name=('parent'),blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    avatar=models.ImageField(blank=True,upload_to='categories/')
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    upload_time=models.DateTimeField(auto_now=True)

    class meta:
        db_table='categories'
        verbose_name=('Category')
        verbose_name_plural=('Categories')

class Product(models.Model):
    
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    avatar=models.ImageField(blank=True,upload_to='products/')
    is_enable=models.BooleanField(default=True)
    categories=models.ManyToManyField('Category',blank=True,verbose_name=('categories'))
    created_time=models.DateTimeField(auto_now_add=True)
    upload_time=models.DateTimeField(auto_now=True)

    class meta:
        db_table='products'
        verbose_name=('product')
        verbose_name_plural=('products')



class File(models.Model):
     
    product=models.ForeignKey('product',on_delete=models.CASCADE,verbose_name=('product'))
    title=models.CharField(('title'),max_length=50)
    file=models.FileField(('file'),upload_to='files/%Y/%m/%d/')
    is_enable=models.BooleanField(('is_enable'),default=True)
    created_time=models.DateTimeField(('created_time'),auto_now_add=True)
    upload_time=models.DateTimeField(('upload_time'),auto_now=True)
    
    class meta:
        db_table='files'
        verbose_name=('file')
        verbose_name_plural=('files')
