from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm 

urlpatterns = [
    path('',views.ProductView.as_view(),name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('profile/',views.profile,name='profile'),
    path('registration/',views.CustomerRegistrationView.as_view(),name='registration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='home/login.html',authentication_form=LoginForm),name='login'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)