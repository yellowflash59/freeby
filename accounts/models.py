from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.urls import reverse

class UserStripe(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    stripe_id=models.CharField(max_length=120,null=True,blank=True)

    def __str__(self):
        return str(self.stripe_id)

class EmailConfirmed(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    activation_key=models.CharField(max_length=200)
    confirmed=models.BooleanField(default=False)

    def __str__(self):
        return str(self.confirmed)

    def activate_user_email(self):
    #send email here & render a string
        activation_url="{}/{}".format(settings.SITE_URL,reverse('activation_view',args=[self.activation_key]))
        context = {
        	"activation_key": self.activation_key,
        	"activation_url": activation_url,
        	"user": self.user.username,
        }
        message = render_to_string("accounts/activation_message.txt", context)
        subject = "Activate your Email"

        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.user.email], **kwargs)

class EmailMarketingSignup(models.Model):
    email=models.EmailField()
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    confirmed=models.BooleanField(default=False)

    def __str__(self):
        return str(self.email)

class UserDefaultAddress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    shipping = models.ForeignKey("UserAddress",on_delete=models.CASCADE,null=True,\
                blank=True,related_name="user_address_shipping_default")
    billing = models.ForeignKey("UserAddress",on_delete=models.CASCADE,\
                null=True,blank=True,related_name="user_address_billing_default")
    def __str__(self):
        return str(self.user.username)

class UserAdreesManager(models.Manager):
    def get_billing_addresses(self,user):
        return super(UserAdreesManager,self).filter(billing=True).filter(user=user)


class UserAddress(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    address=models.CharField(max_length=120)
    address2=models.CharField(max_length=120,null=True,blank=True)
    city=models.CharField(max_length=120)
    state=models.CharField(max_length=120,null=True,blank=True)
    country=models.CharField(max_length=120)
    zipcode=models.CharField(max_length=25)
    phone=models.CharField(max_length=120)
    shipping=models.BooleanField(default=True)
    billing=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    class Meta:
        ordering=['-updated','-timestamp']

    def __str__(self):
        return str(self.user.username)

    def get_address(self):
        return "{} {} {} {} {}".format(self.address,self.city,self.state,self.country,self.zipcode)

    objects=UserAdreesManager()
