from django.shortcuts import render,Http404
from .models import Product,ProductImage
from marketing.models import  MarketingMessage,Slider
# Create your views here.
def search(request):
    try:
        q=request.GET.get('q')
    except:
        q = None
    if q:
        products=Product.objects.filter(title__icontains=q)
        context={'query':q,'products':products}
        template='products/result.html'
    else:
        template='products/home.html'
        context={}
    return render(request,template,context)

def home(request):
    sliders=Slider.objects.all_featured()
    products=Product.objects.all()
    template='products/home.html'
    context={'products':products,
    'sliders':sliders,
    }
    return render(request,template,context)

def all(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    template='products/all.html'
    return render(request,template,context)

def single(request,slug):
    #try:
        product=Product.objects.get(slug=slug)
        #image=product.productimage_set.all()
        images=ProductImage.objects.filter(product=product)
        context={
            'product':product,
            'images':images
        }
        template='products/single.html'
        return render(request,template,context)
    #except:
        raise Http404
