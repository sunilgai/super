# Generated by Django 4.0.3 on 2022-03-29 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exportapp', '0013_rename_decorative_products_handicraft_image_handicraft_decorative_products_decorative_handicraft_ima'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homesliding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_titile', models.TextField(max_length=300)),
                ('one_image', models.ImageField(upload_to='homesliding')),
                ('two_titile', models.TextField(max_length=300)),
                ('two_image', models.ImageField(upload_to='homesliding')),
                ('three_titile', models.TextField(max_length=300)),
                ('three_image', models.ImageField(upload_to='homesliding')),
                ('four_titile', models.TextField(max_length=300)),
                ('four_image', models.ImageField(upload_to='homesliding')),
            ],
        ),
    ]
