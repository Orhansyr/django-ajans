from django.db import models
from django.contrib import admin
from tinymce.models import HTMLField
from django.utils.html import format_html


class ProductCategory(models.Model):
    title = models.CharField('Kategori Adı', max_length=100)
    slug = models.SlugField('slug', max_length=100, unique=True)
    image = models.ImageField('Kategori Resmi', upload_to='category_images/')
     
    @admin.display(description="Kategori Resmi")
    def image_tag(self):
        if self.image:
            return format_html(
                '<img src="{}" width="170" height="170" />', self.image.url
            )
        return "Görsel yok"


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'


class Product(models.Model):
    title = models.CharField('isim', max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    content = HTMLField('Açıklama')
    content2 = HTMLField('Açıklama-2')
    slug = models.SlugField('slug', max_length=100, unique=True)
    meta_title = models.CharField('Meta Title', max_length=100)
    meta_description = models.CharField('Meta Description', max_length=255)
    miktar = models.IntegerField('Adet')
    stok = models.BooleanField('Stok Durumu', default=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'


class product_image(models.Model):
    title = models.CharField('Başlık', max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Resim', upload_to='product_images/')

    def __str__(self):
        return f"{self.product.name} - Resim"
    
    class Meta:
        verbose_name = 'Ürün Resmi'
        verbose_name_plural = 'Ürün Resimleri'

    @admin.display(description="Ürün Resmi")
    def image_tag(self):
        if self.image:
            return format_html(
                '<img src="{}" width="170" height="170" />', self.image.url
            )
        return "Görsel yok"    


# Sayfa soyut sınıfı, diğer sayfa türleri için temel oluşturacak
class page(models.Model):
    title = models.CharField('Başlık', max_length=100)
    content = HTMLField('Açıklama')
    slug = models.SlugField('slug', max_length=100, unique=True)
    meta_title = models.CharField('Meta Title', max_length=100)
    meta_description = models.CharField('Meta Description', max_length=255)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Sayfa'
        verbose_name_plural = 'Sayfalar'
        abstract = True

    
class AboutPage(page):
    image = models.ImageField('Resim', upload_to='page_images/')

    def __str__(self):
        return self.title

    @admin.display(description="Hakkımızda Resmi")
    def image_tag(self):  
        if self.image:
            return format_html(
                '<img src="{}" width="170" height="170" />', self.image.url
            )
        return "Görsel yok"
        







'''
class Hero(models.Model):
    title = models.CharField('Başlık', max_length=100)
    description = HTMLField('Açıklama')
    image = models.ImageField('Resim', upload_to='hero_images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Hero'

    @admin.display(description="Hero Resmi")
    def image_tag(self):
        if self.image:
            return format_html(
                '<img src="{}" width="170" height="170" />', self.image.url
            )
        return "Görsel yok"        
'''