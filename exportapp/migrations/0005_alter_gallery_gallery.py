# Generated by Django 4.0.3 on 2022-03-25 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exportapp', '0004_rename_gallery_gallery_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery',
            field=models.ImageField(upload_to='mygallery'),
        ),
    ]