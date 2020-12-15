from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'logout/$',views.logout_view,name='auth_logout'),
    url(r'login/$',views.login_view,name='auth_login'),
    url(r'register/$',views.registration_view,name='auth_register'),
    url(r'activate/(?P<activation_key>\w+)/$',views.activation_view,name='activation_view'),
    url(r'^ajax/add_user_address/$',views.add_user_address,name='ajax_add_user_address')
]
