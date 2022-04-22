


from distutils.command.upload import upload
from django.db import models


from django.core.validators import FileExtensionValidator


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    number = models.CharField(max_length=50,null=True)
    message = models.CharField(max_length=210,null=True)
  
 
class Gallery(models.Model):
   gallery = models.ImageField(upload_to="mygallery")


class Blog(models.Model):
    image = models.ImageField(upload_to="myimage")
    title = models.CharField(max_length=50,null=True)
    description = models.TextField(max_length=500,null=True)

class Key_person(models.Model):
    image = models.ImageField(upload_to="myprofile",null=True)
    name = models.CharField(max_length=50,null=True)
    equcation = models.CharField(max_length=50,null=True)
    sub_title = models.CharField(max_length=100,null=True)
    facebooklinks = models.CharField(max_length=300,null=True)
    instagramlinks = models.CharField(max_length=300,null=True)
    linkedinlinks = models.CharField(max_length=300,null=True)
    twitterlinks = models.CharField(max_length=300,null=True)
    youtubelinks = models.CharField(max_length=300,null=True)
    description = models.TextField(max_length=1000,null=True)

class Contact_page(models.Model):
    title = models.CharField(max_length=100,null=True)
    discription = models.TextField(max_length=500,null=True)
    email_id = models.EmailField(max_length=100,null=True)
    Contact_details = models.CharField(max_length=100)
    Address = models.TextField(max_length=200,null=True)
    heading = models.CharField(max_length=100)
    facebookicon = models.ImageField(upload_to="mysocialmediaicon",null=True)
    instagramicon = models.ImageField(upload_to="mysocialmediaicon",null=True)
    linkedinicon = models.ImageField(upload_to="mysocialmediaicon",null=True)
    twittericon = models.ImageField(upload_to="mysocialmediaicon",null=True)
 

class Clients (models.Model):
    image = models.ImageField(upload_to="clients")
    name = models.CharField(max_length=50)
    company_country = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

class About_company(models.Model):
    description = models.TextField(max_length=1000)
    sub_description = models.TextField(max_length=1000)
    
class Incense_Sticks(models.Model):
    image = models.ImageField(upload_to="incense")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
class Incense_photos(models.Model):
    image = models.ImageField(upload_to="incense")
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,null=True)

  
class Candles(models.Model):
    image = models.ImageField(upload_to="candles")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
class Candles_photos(models.Model):
    image = models.ImageField(upload_to="candles")
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,null=True)

  


class Wood_products(models.Model):
    image = models.ImageField(upload_to="wood")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
   
   
class wood_products_photos(models.Model):
    image = models.ImageField(upload_to="wood")
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,null=True)


class Clay_products(models.Model):
    image = models.ImageField(upload_to="clay")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
class Clay_products_photos(models.Model):
    image = models.ImageField(upload_to="clay")
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,null=True)

class Bamboo_products(models.Model):
    image = models.ImageField(upload_to="bamboo")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
class Bamboo_products_photos(models.Model):
    image = models.ImageField(upload_to="bamboo")
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,null=True)


class Love_for_Clients1(models.Model):
    image = models.ImageField(upload_to="clients")
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)


class Love_for_Clients2(models.Model):
    image = models.ImageField(upload_to="clients")
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)


class Love_for_Clients3(models.Model):
    image = models.ImageField(upload_to="clients")
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)


class Love_for_Clients4(models.Model):
    image = models.ImageField(upload_to="clients")
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
