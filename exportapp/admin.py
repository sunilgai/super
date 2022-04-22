from django.contrib import admin
from .models import Contact, Contact_page, Gallery, Blog,Key_person,Contact_page,About_company,Incense_Sticks,Incense_photos,Candles,Candles_photos,Wood_products,wood_products_photos,Bamboo_products,Bamboo_products_photos,Clay_products,Clay_products_photos,Love_for_Clients1,Love_for_Clients2,Love_for_Clients3,Love_for_Clients4
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','number','message']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display= ['id','gallery']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display= ['id','image','title','description']

@admin.register(Key_person)
class Key_personAdmin(admin.ModelAdmin):
    list_display= ['id','image','name','equcation','sub_title','facebooklinks','instagramlinks','linkedinlinks','twitterlinks','youtubelinks','description']


@admin.register(Contact_page)
class Contact_pageAdmin(admin.ModelAdmin):
    list_display= ['id','title','discription','email_id','Contact_details','Address','heading','facebookicon','instagramicon','linkedinicon','twittericon']



@admin.register(About_company)
class About_companyAdmin(admin.ModelAdmin):
    list_display = ['id','description','sub_description']


@admin.register(Incense_Sticks)
class Incense_SticksAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']


@admin.register(Incense_photos)
class Incense_photosAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']


@admin.register(Candles)
class CandlesAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']


@admin.register(Candles_photos)
class Candles_photosAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']




@admin.register(Wood_products)
class Wood_productsAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']


@admin.register(wood_products_photos)
class wood_products_photosAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']


@admin.register(Bamboo_products)
class Bamboo_productsAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']


@admin.register(Bamboo_products_photos)
class Bamboo_products_photosAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']


@admin.register(Clay_products)
class Clay_productsAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']


@admin.register(Clay_products_photos)
class Clay_products_photosAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']


@admin.register(Love_for_Clients1)
class Love_for_Clients1Admin(admin.ModelAdmin):
    list_display= ['id','image','name','country','description']


@admin.register(Love_for_Clients2)
class Love_for_Clients2Admin(admin.ModelAdmin):
    list_display= ['id','image','name','country','description']


@admin.register(Love_for_Clients3)
class Love_for_Clients3Admin(admin.ModelAdmin):
    list_display= ['id','image','name','country','description']


@admin.register(Love_for_Clients4)
class Love_for_Clients4Admin(admin.ModelAdmin):
    list_display= ['id','image','name','country','description']

