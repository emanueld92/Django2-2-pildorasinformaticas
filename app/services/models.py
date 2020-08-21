from django.db import models

# Create your models here.

class service(models.Model):
    title=models.CharField('Titulo', blank=False, null=True , max_length=50)
    content=models.TextField('Contenido', blank=False, null=True, max_length=100)
    img= models.URLField('imagen',blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Servicios"
        verbose_name= "Servicio"

    def __str__(self):
        return self.title