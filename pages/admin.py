from django.contrib import admin
from .models import Product_Category, Product, Product_image, About_Page,Page_Image



@admin.register(Product_Category)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)

class AboutImageAdmin(admin.TabularInline):
    model = Page_Image
    extra = 2
    readonly_fields = ('image_tag',)


@admin.register(About_Page)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    inlines = [AboutImageAdmin]    


class ProductImageAdmin(admin.TabularInline):
    model = Product_image
    extra = 2
    readonly_fields = ('image_tag',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', "category",)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageAdmin]



    








