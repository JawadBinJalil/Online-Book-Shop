from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICE=[
    ('N','Novel'),
    ('P','Poem'),
    ('S','Story'),
]

class product(models.Model):
    title=models.CharField(max_length=100)
    prize=models.FloatField()
    image=models.ImageField(upload_to='product')
    category=models.CharField(choices=CATEGORY_CHOICE,max_length=2)

    def __str__(self):
        return str(self.id)
    
class offers(models.Model):
    title_of_offers=models.CharField(max_length=10,default='')
    image_of_offers=models.ImageField(upload_to='offer',default='')

    def __str__(self):
        return str(self.id)
    

    

