from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título") #Tipo: Cadena de carácteres <255 caracteres (VARCHAR2(200))
    description = models.TextField(verbose_name="Descripción") #Tipo: Texto puede tener >255 caracteres
    image = models.ImageField(verbose_name="Imagen",upload_to="projects") #Tipo: Imagen. upload_to lo que hara es crear un directorio project en la carpeta media(configurada en settings.py) para almacenar las imagenes de este modelo
    #Tipo: Fecha
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación") # Se añade la hora actual cuando se crea automáticamente
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición") # Se añade la hora cuando se modifica
    # La diferencia entre auto_now_add y auto_now es que el segundo se 
    # ejecuta cada vez que se actualiza el objeto y el otro solo cuando se crea
    url = models.URLField(verbose_name="Dirección Web",null=True,blank=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] # Ordenar por creación. Si se pone el - delante, ordena del mas nuevo al más antiguo

    def __str__(self): # como si fuera un toString en python
        return self.title