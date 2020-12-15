from django.contrib import admin
from .models import Product,ProductImage,Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields=['title','description']
    list_display=['__str__','price','active','updated']
    list_editable=['price','active']
    readonly_fields=['timestamp','updated']
    prepopulated_fields={"slug":("title",)}
    class Meta:
        model=Product


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variation)
