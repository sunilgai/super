from asyncio import futures
from django.shortcuts import render
from .models import Contact, Contact_page, Gallery, Blog,Key_person,Contact_page,About_company,Incense_Sticks,Incense_photos,Candles,Candles_photos,Wood_products,wood_products_photos,Bamboo_products,Bamboo_products_photos,Clay_products,Clay_products_photos,Love_for_Clients1,Love_for_Clients2,Love_for_Clients3,Love_for_Clients4

# Create your views here.
def about_index (request):
     company = About_company.objects.all()
     return render (request, 'about-company/index.html',{'company':company})
     
def index (request):
     if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        message=request.POST.get('message')
        reg= Contact(name=name,email=email,number=number,message=message)
        reg.save()
        return render(request,'index.html')
     else:
          pic = Gallery.objects.all()
          Key = Key_person.objects.all()
          client1 = Love_for_Clients1.objects.all()
          client2 = Love_for_Clients2.objects.all()
          client3 = Love_for_Clients3.objects.all()
          client4 = Love_for_Clients4.objects.all()
         
          return render (request, 'index.html',{'pic':pic,'key':Key,'client1':client1,'client2':client2,'client3':client3,'client4': client4})

         
         






    
def blog (request):
     gal = Blog.objects.all()
     Key = Key_person.objects.all()
     return render (request, 'blog/index.html', {'gal':gal,'key':Key})



def certification (request):
     Key = Key_person.objects.all()

     return render (request, 'certification/index.html',{'key':Key})



def contact (request):

    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        message=request.POST.get('message')
        reg= Contact(name=name,email=email,number=number,message=message)
        reg.save()
        
        return render(request,'contact-us/index.html')
    else:
       con = Contact_page.objects.all()  
       Key = Key_person.objects.all()
       return render(request,'contact-us/index.html',{'con':con,'key':Key})



def gallery (request):
     pic = Gallery.objects.all()
     Key = Key_person.objects.all()
     return render (request, 'gallery/index.html',{'pic':pic,'key':Key})


  





def sourcing_agent(request):
     Key = Key_person.objects.all()
     return render (request, 'sourcing-agent/index.html',{'key':Key})





def key_person (request):
     Key = Key_person.objects.all()
     return render (request, 'key-person/index.html',{'key':Key})


def incense (request):
     incense = Incense_Sticks.objects.all()
     incense1 = Incense_photos.objects.all()
     return render (request, 'incence.html',{'incense':incense,'incense1':incense1})



def candles (request):
     candles = Candles.objects.all()
     candles1 = Candles_photos.objects.all()
     return render (request,'candle.html',{'candles':candles,'candles1':candles1})





def wood (request):
     wood = Wood_products.objects.all()
     wood1 = wood_products_photos.objects.all()
     return render (request,'wood.html',{'wood':wood,'wood1':wood1})



def bamboo (request):
     bamboo = Bamboo_products.objects.all()
     bamboo1 =Bamboo_products_photos.objects.all()
     return render (request,'bamboo.html',{'bamboo':bamboo,'bamboo1':bamboo1})



def clay (request):
     clay = Clay_products.objects.all()
     clay1 = Clay_products_photos.objects.all()
     return render (request,'clay.html',{'clay':clay,'clay1':clay1})