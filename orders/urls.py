from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^checkout/$',views.checkout,name='checkout'),
    url(r'^orders/$',views.orders,name='user_orders')
]
