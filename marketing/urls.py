from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^ajax/dismiss_marketing_message/$',views.dismiss_marketing_message,name='dismiss_marketing_message'),
    url(r'^ajax/email_signup/$',views.email_signup,name='ajax_email_signup'),
]
