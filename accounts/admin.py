from django.contrib import admin
from .models import UserStripe,EmailConfirmed,EmailMarketingSignup,UserAddress,UserDefaultAddress
# Register your models here.
class UserAddressAdmin(admin.ModelAdmin):
    class Meta:
        model=UserAddress
admin.site.register(UserAddress,UserAddressAdmin)

admin.site.register(UserStripe)
admin.site.register(EmailConfirmed)

class EmailMarketingSignupAdmin(admin.ModelAdmin):
    list_display=['__str__','timestamp']
    class Meta:
        model=EmailMarketingSignup

admin.site.register(EmailMarketingSignup,EmailMarketingSignupAdmin)

admin.site.register(UserDefaultAddress)
