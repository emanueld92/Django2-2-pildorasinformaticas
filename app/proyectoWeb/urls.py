from django.urls import path
#from proyectoweb.views import index

from app.proyectoWeb import views
urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('store', views.store, name='store'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
]