# Generated by Django 5.0.1 on 2024-01-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_offers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='offers',
        ),
        migrations.AddField(
            model_name='product',
            name='image_of_offers',
            field=models.ImageField(default='', upload_to='offer'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_of_offers',
            field=models.CharField(default='', max_length=10),
        ),
    ]