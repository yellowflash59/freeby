from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^s/$',views.search,name='search'),
    url(r'^products/$',views.all,name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$',views.single,name='single_product'),

]
