from django.shortcuts import render
from django.views import View
from .models import product,offers
from .forms import CustomerRegistration
from django.contrib import messages
# Create your views here.
class ProductView(View):
    def get(self,request):
        Novel=product.objects.filter(category='N')
        Poem=product.objects.filter(category='P')
        Story=product.objects.filter(category='S')
        discount=offers.objects.all()
        
        return render(request,'home/home.html',{'Novel':Novel,'Poem':Poem,'Story':Story,'discount':discount})
    
def aboutus(request):
    return render(request,'home/about_us.html')
    

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistration()
        return render(request,'home/customerregistration.html',{'form':form})
    
    def post(self,request):
        form=CustomerRegistration(request.POST)
        if form.is_valid():
            messages.success(request,"Successfully Registration Done")
            form.save()
        return render(request,'home/customerregistration.html',{'form':form})
    
def profile(request):
 return render(request, 'home/profile.html')


        