# Generated by Django 4.0.3 on 2022-03-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exportapp', '0008_contact_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_page',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
