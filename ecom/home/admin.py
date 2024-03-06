from django.contrib import admin
from .models import product,offers

# Register your models here.
@admin.register(product)
class productModelAdmin(admin.ModelAdmin):
    list_display =['title', 'prize', 'category','image']

@admin.register(offers)
class productModelAdmin(admin.ModelAdmin):
    list_display =['title_of_offers','image_of_offers']