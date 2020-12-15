from django.db import models


# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=120,null=False,blank=False)
    description=models.TextField(null=True,blank=False)
    price=models.DecimalField(decimal_places=2,max_digits=10,default=12.99)
    sale_price=models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    slug=models.SlugField(unique=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together=['title','slug']

    def get_price(self):
        return self.price

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products/images/')
    featured=models.BooleanField(default=True)
    thumbnail=models.BooleanField(default=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.product.title

class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager,self).filter(active=True)
    def sizes(self):
        return self.all().filter(category='size')
    def colors(self):
        return self.all().filter(category='color')


VAR_CATEGORIES=(
    ('size', 'size'),
    ('color','color'),
    ('package','package'),
)

class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    image=models.ForeignKey(ProductImage,null=True,blank=True,on_delete=models.CASCADE)
    category=models.CharField(max_length=200,choices=VAR_CATEGORIES,default='size')
    price=models.DecimalField(null=True,blank=True,max_digits=100,decimal_places=2)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    active=models.BooleanField(default=True)

    objects=VariationManager()

    def __str__(self):
        return self.title
