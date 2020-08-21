from django.shortcuts import render, HttpResponse



def home(request):
    return render(request,"proyectoWeb/home.html") 

def services(request):
    return render(request,"proyectoWeb/services.html")

def store(request):
    return render(request,"proyectoWeb/store.html")

def contact(request):   
    return render(request,"proyectoWeb/contact.html")

def blog(request):
    return render(request,"proyectoWeb/blog.html")