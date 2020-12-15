import re
from django.shortcuts import render,HttpResponseRedirect,Http404
from django.contrib.auth import logout,login,authenticate
from .forms import LoginForm,RegistrationForm,UserAddressForm
from .models import EmailConfirmed,UserDefaultAddress
from django.contrib import messages
from django.urls import reverse
# Create your views here.
def logout_view(request):
    logout(request)
    messages.success(request,"successfully logged Out, Feel free to <a href='{}'>login</a> again".format(reverse("auth_login")),extra_tags='safe')
    return HttpResponseRedirect('{}'.format("auth_login"))

def login_view(request):
    form=LoginForm(request.POST or None)
    btn="Login"
    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        login(request,user)
        messages.success(request,"successfully logged In,welcome again")
        return HttpResponseRedirect("/")
        # user.emailconfirmed.activate_user_email()
    context={
        "form":form,
        "submit_btn":btn
    }
    return render(request,"form.html",context)

def registration_view(request):
    btn="join"
    form=RegistrationForm(request.POST or None)
    if form.is_valid():
        print("is valid")
        new_user=form.save(commit=False)
        new_user.save()
        messages.success(request,"successfully Registered,please confirm your email now.")
        return HttpResponseRedirect("/")
    context={
        "form":form,
        "submit_btn":btn
    }
    return render(request,"form.html",context)

SHA1_RE=re.compile('^[a-f0-9]{40}$')
def activation_view(request,activation_key):
    if SHA1_RE.search(activation_key):
        print("activation key is real")
        try:
            instance=EmailConfirmed.objects.get(activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            instance=None
            return HttpResponseRedirect("/")
        if instance is not None and not instance.confirmed:
            page_message="user has been confirmed"
            instance.confirmed=True
            instance.activation_key="Confirmed"
            instance.save()
        elif instance is not None and  instance.confirmed:
            page_message="already confirmed"
        else:
            page_message=""
        context={
            "page_message":page_message
        }
        return render(request,"accounts/activation_complete.html",context)
    else:
        raise Http404

def add_user_address(request):
    print(request.GET)
    try:
        next_page=request.GET.get("next")
    except:
        next_page=None
    if request.method=="POST":
        form=UserAddressForm(request.POST)
        if form.is_valid:
            new_address=form.save(commit=False)
            new_address.user=request.user
            new_address.save()
            is_default=form.cleaned_data["default"]
            if is_default:
                default_address,created=UserDefaultAddress.objects.get_or_create(user=request.user)
                default_address.shipping=new_address
                default_address.save()
            if next_page is not None:
                return HttpResponseRedirect(reverse(str(next_page))+"?address_added=True")
    else:
        raise Http404
