from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
from datetime import datetime

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if not name:
            return HttpResponse("Name field is required!", status=400)

        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Save to database
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your Request is submitted!")

    return render(request, "contact.html")