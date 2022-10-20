# PersonalWebPython
Formación en Python - Django Marcos Ruiz Muñoz

# Introducción

Django es un framework web programado en Python.
Características:
- Tiene un sistema basado en componentes reutilizables, las "apps"
- Un mapeador ORM para manejar registros de la BD
- Un panel de administrador extensible ya creado
- Un potente sistema de plantillas extensibles con herencia
- Sesiones, formularios, internacionalización, etc.

# Entornos virtuales: Virtualenv vs Pipenv
Permiten gestionar diferentes versiones de los paquetes.

Virtualenv: gestiona entorno global
Pipenv: gestiona el entorno del proyecto

## Instalar pipenv

<pre><code>
pip install pipenv
</pre></code>

Uso de pipenv
- Crear un entorno virtual vacío que permitirá trabajar con distintas versiones de paquete para un proyecto: Acceder al directorio del proyecto y ejecutar

<pre><code>pipenv --python 3.10.8</pre></code>
(siempre la versión que se tenga pyhon --version)

- Encontrar el entorno virtual:

<pre><code>pipenv --venv</pre></code>

- Aquí se encuentran los paquetes instalados en el entorno virtual. Para encontrar por ejemplo el ejecutable de python, se podría escribir:
<pre><code>pipenv --py</pre></code>

- Para acceder al python del entorno virtual, ejecutar:

<pre><code>pipenv run python</pre></code>

- Instalar un paquete/módulo

<pre><code>pipenv install numpy</pre></code>
<p>
o 
</p>
<pre><code>pipenv pip install numpy</pre></code>

- Mostrar los paquetes instalados en el entorno virtual:
<pre><code>pipenv graph</pre></code>

- Desinstalar un paquete/módulo
<pre><code>pipenv uninstall numpy</pre></code>
<p>
o 
</p>
<pre><code>pipenv pip uninstall numpy</pre></code>

- Borrar entorno virtual
<pre><code>pipenv --rm</pre></code>

Los entornos virtuales de pipenv quedan enlazados al directorio del proyecto. Si se cambia de ubicación o de nombre, deja de tener uso el entorno virtual.

## Crear primer proyecto con Pipenv

1. Ejecutar el comando con todas los paquetes que se van a utilizar:
<pre><code>pipenv install django django-ckeditor Pillow pylint pylint-django pylint-celery</pre></code>

django-ckeditor: para editar campos de texto en el panel de administrador
Pillow: para la gestión de imágenes
pylint: linting para mostrar los errores de código

2. Ver ubicación del entorno virtual con pipenv -venv
3. Ejecutar <b>pipenv run django-admin</b> para ver los comandos django y ver el de start project
4. Iniciar un nuevo proyecto: <b>pipenv run django-admin startproject personalwebsite</b>
5. Activar entorno pipenv: <b>pipenv shell</b>
6. Ejecutar el servidor Django: <b>python manage.py runserver</b>
Una forma alternativa es editar el archivo Pipfile poniendo al final:

<pre><code>
[scripts]
personalwebsite = "python personalwebsite/manage.py runserver"
</pre></code>

y de esta forma se podrá ejecutar el servidor desde el directorio anterior el comando <b>pipenv run personalwebsite</b>

## Configuración inicial del proyecto

https://docs.hektorprofe.net/django/web-personal/configurando-proyecto/

1. Manage.py: script para gestionar el proyecto desde la terminal
2. __init__.py: indica que la carpeta es un paquete
3. settings.py: configuración del proyecto
4. urls.py: encargado de manejar las direcciones de la web
5. wsgi.py: contiene la información para desplegar el proyecto en producción
6. En settings.py, el modo DEBUG=True es un modo de ejecución en el que cuando ocurre un fallo, Django dará información para solucionarlo. Por lo tanto,
es para ponerlo en desarollo y no en producción. SI se cambia LANGUAGE_CODE = 'es' mostrará en español

## Crear la base de datos inicial
Django trabaja con bases de datos SQL.
Al ejecutar el servidor  del proyecto, saldrá un mensaje: You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, 
contenttypes, sessions.
Con el comando <b>python manage.py migrate</b> se migrará la base de datos y se sincronizará con el proyecto.

Se configura dentro de settings.py, en el apartado DATABASES, pudiendo cambiarse a postgreSQL,Oracle,etc.

## Primera App [Core] Vistas
Django tiene un sistema de "Apps" aplicaciones internas de Django. Estas apps son: admin, auth, contenttypes, sessions. Estas apps sirven para manejar la
autenticación de los usuarios y se encuentran configuradas en el settings.py en INSTALLED_APPS.
Se pueden crear apps propias para reutilizarlas en otros proyectos.

Para crear la primera app:
- Ejecutar el comando <b>python manage.py startapp core</b>
- En la carpeta creada, editar la carpeta <b>views.py</b> para crear el siguiente método que devolverá un código HTML de la página.
<pre><code>
from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("<h1>My personal website</h1><h2>Cover Page</h2>")
</pre></code>

- Configurar la URL para que se muestre la vista. Para esto, editar el archivo <b>urls.py</b>, en el urlpatterns.

from django.contrib import admin
from django.urls import path
from core import views

<pre><code>
urlpatterns = [
    path('',views.home,name="home"),
    path('admin/', admin.site.urls),
]
</pre></code>

## Templates

1. Crear un directorio templates.
2. Dentro se tendrá que crear un nuevo directorio con el mismo nombre de la app (core).
3. Para usar esta plantilla, se utilizará la función <b>render(request,core/plantilla.html)</b> en el views.py importada por defecto.
4. Para que django cargue las plantillas, añadir en settings.py la app <b>Core</b> que se ha creado en INSTALLED_APPS 

### Herencia de templates

- La plantilla padre tendrá la anotación {% block <nombre> %} {% endblock <nombre> %} Por ejemplo:

<pre><code>
<body>
    <!-- MENU -->
    <h1>My personal website</h2>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about-me">About me</a></li>
            <li><a href="/portfolio">Portfolio</a></li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    <!-- CONTENT -->
    {% block content %} {% endblock %}
</body>
</pre></code>

- La plantilla hijo tendrá que usar la anotación {% extends 'core/header.html' %} para tener la plantilla padre y asignar su contenido al padre con 
la anotación {% block <nombre> %} {% endblock <nombre> %} Ejemplo:

<pre><code>
{% extends 'core/header.html' %}


{% block content %}
<h2>Home</h2>
<p>
    This is the Home
</p>
{% endblock content %}
</pre></code>

### Template Tag URL

- En urls.py se tienen las diferentes rutas y en cada ruta se le asigna una variable name que puede ser usada en las templates, por ejemplo:

<b>urls.py</b>
<pre><code>
urlpatterns = [
    path('',views.home,name="home"),
]
</pre></code>

<b>header.html</b>
<pre><code>
    <h1>My personal website</h2>
        <ul>
            <li><a href="{% url 'home' %}">Home</a></li>
            <li><a href="{% url 'about' %}">About me</a></li>
			....
        </ul>
</pre></code>

### Más Template Tags
<p>
Hay más template Tags en la documentación oficial de Django: 
https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#built-in-tag-reference
o en W3Schools: 
https://www.w3schools.com/django/django_template_tags.php
</p>

#### Autoescape
<p>
Escape variables that contain HTML tags: 
<b>{% autoescape on|off %} ... {% endautoescape %}</b>
</p>
[Example Autoescape](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_autoescape_off)


#### Comment
<p>
Insert a comment in the Django code:  
<b>{% comment explanation %}....{% endcomment %}</b>
</p>
[Example Comment](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_comment)


#### Cycle && For

<p>
El ciclo se reinicia cuando llega al final, y continúa hasta que no hay más iteraciones:

<b>{% cycle arg1 arg2 arg3 etc. %}</b>


</p>
[Example Cycle](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_cycle)

#### For & Empty

<b>
{% for item in object %}
{% endfor %}
</b>

[Example For](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_cycle)

- Uso de <b>Empty</b> para comprobar si la lista está vacía
<pre><code>
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
</code></pre>

#### Filter

<p>
La etiqueta de filtro le permite ejecutar una sección de código a través de un filtro, y devolverlo de acuerdo con la(s) palabra(s) clave del filtro.
<b>
{% filter keyword %}
...
{% endfilter %}</b>
</p>

[Example Filter](https://www.w3schools.com/django/ref_tags_filter.php)

#### Firstof
<p>
La etiqueta firstof devuelve el primer argumento que no es una variable vacía.

Las variables vacías pueden ser una cadena vacía "", o un número cero 0, o un booleano false.

<b>{% firstof var1 var2 var3 etc. %}</b>
</p>

Si no es ninguna, se puede poner un elemento de error:
<pre><code>
{% autoescape off %}
    {% firstof var1 var2 var3 "<strong>fallback value</strong>" %}
{% endautoescape %}
</code></pre>

[Example Firstof](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_firstof)

#### If
<p>
<b>
{% if condition %}
{% endif %}</b>
</p>

[Example If](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_if3)

#### IfChanged

<p>
Se usa en bucles. Si dentro del bucle, cambia el valor de la variable seleccionada respecto a la var anterior, entra en el bloque.
<b>
{% ifchanged property %}
...
{% endifchanged %}
</b>
</p>
[Example IfChanged](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_ifchanged2)

#### Include && With

<p>
La etiqueta include le permite incluir contenido de otra plantilla.
Coloque la etiqueta include exactamente donde quiere que se muestre el contenido.
Esto es útil cuando tienes el mismo contenido para muchas páginas.
También puede enviar variables a la plantilla, utilizando la palabra clave with:

<b>
{% include template with key=value%}
</b>
</p>
[Example Include](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_include2)

#### Lorem

<p>
Para insertar texto aleatorio las líneas que se quiera y eligiendo un método (si párrafo p, bloque b o palabras w)

<b>{% lorem count method random %}</b>
</p>

[Example Lorem](https://www.w3schools.com/django/ref_tags_lorem.php)

#### Now

<p>
Introduce la fecha actual en un formato específico.
<b>{% now format %}</b>
</p>
[Example Now](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_now2)

#### Regroup

<p>
La etiqueta regroup devuelve un nuevo objeto agrupado por un valor especificado.

El resultado se divide en un objeto llamado GroupedResult que tiene las propiedades grouper: la propiedad que se ha seleccionado para agrupar
y list que son los demás valores.

<b>{% regroup object by object.property as newname %}</b>
</p>
[Example Now](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_regroup)

#### ResetCycle

<p>
La etiqueta resetcycle se utiliza dentro de un ciclo, y reinicia el ciclo, haciendo que empiece desde el principio para el siguiente elemento.

No reinicia el bucle, sólo el ciclo.
<b>{% resetcycle name %}</b>
</p>
[Example Now](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_resetcycle2)

#### Spaceless

<p>
La etiqueta spaceless se utiliza para eliminar cualquier espacio entre etiquetas, en el código.

La etiqueta spaceless elimina los espacios en blanco, las nuevas líneas y los tabuladores.

<b>{
% spaceless %}...{% endspaceless %}</b>
</p>

[Example Spaceless](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_spaceless)

#### TemplateTag

<p>
La etiqueta templatetag se utiliza para mostrar los caracteres que normalmente se utilizan para realizar las tareas de Django.

Cada carácter de la etiqueta, como {{, {% y {#, tiene su propio nombre, véase más abajo.

<b>{% templatetag name %}</b>
</p>
[Example TemplateTag](https://www.w3schools.com/django/showdjango.php?filename=demo_tags_templatetag)

### Request Path

Todas las templates tienen una variable llamada request.path que indica la url de la página.

<pre><code>
 {% if request.path != '/'%}
	<hr>
 {% endif %}
</code></pre>

## App para manejar el panel de administrador y Modelos en Base de datos

### Crear Modelo y Migrar base de datos y modelo
Crear la app con el comando <b>python manage.py startapp portfolio</b>

El script <b>models.py</b> es donde se van a crear los modelos, las clases de base de datos.

Para crear un modelo:
1. Se necesitan crear clases en ese archivo que hereden de models.Model:

<pre><code>
class Project(models.Model):
    title = models.CharField(max_length=200) #Tipo: Cadena de carácteres <255 caracteres
    description = models.TextField() #Tipo: Texto puede tener >255 caracteres
    image = models.ImageField() #Tipo: Imagen
    #Tipo: Fecha
    created = models.DateTimeField(auto_now_add=True) # Se añade la hora actual cuando se crea automáticamente
    updated = models.DateTimeField(auto_now=True) # Se añade la hora cuando se modifica
    # La diferencia entre auto_now_add y auto_now es que el segundo se 
    # ejecuta cada vez que se actualiza el objeto y el otro solo cuando se crea
</code></pre>

2. Añadir la nueva app a <p>settings.py</p> en INSTALLED_APPS
3. Migrar el modelo a la base de datos. Se necesitará utilizar dos comandos:

- <b>python manage.py makemigrations portfolio</b>: Sirve para indicar a Django que hay cambios en un modelo para que cree un fichero de migraciones/backup para poder restaurarlo
- <b>python manage.py migrate portfolio</b>: Aplicar la migración a la base de datos

<b>Siempre que haya un cambio en el modelo, es necesario ejecutar estas dos sentencias.</b>

### Tipos de campos

Los modelos en Django permiten defiir multitud de tipos de datos, desde cadenas a enteros, pasando por fechas y horas.
Tipos de datos:https://www.webforefront.com/django/modeldatatypesandvalidation.html

### Opciones de campos

Django también tiene sus propios atributos. Estas opciones establecen configuraciones extendidas como permitir valores nulos o valores por defecto.
Tipos: https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options

### Panel de administrador.

1. Crear el administrador con el comando: <b>python manage.py createsuperuser</b>
2. Acceder con: localhost/admin
3. Activar el modelo en el administrador. Para ello, hay que ir al archivo admin.py de portfolio e importar el modelo para registrarlo al panel:

<pre><code>
from django.contrib import admin
from .models import Project

# Register your models here.
admin.site.register(Project)
</code></pre>

Ahora en el panel de administrador saldrá los proyectos y la app Portfolio.

#### Cambiar el nombre de la app en el panel de administrador

Para cambiar el nombre de la app en el panel de administrador, es necesario modificar el archivo apps.py de portfolio y poner un verbose_name:

<pre><code>

class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = "Portafolio"
</code></pre>

Es necesario que Django utilice esta configuración. Para indicarse, dirigirse al settings.py y en INSTALLED_APPS modificar portfolio por 'portfolio.apps.PortfolioConfig'
<pre><code>

INSTALLED_APPS = [
	.....
    'core',
    'portfolio.apps.PortfolioConfig'
]

</code></pre>


#### Cambiar el nombre del modelo en el panel de administrador

Para cambiar el nombre es necesario modificar el modelo Project de models.py y modificar la clase añadiendo una clase interna llamada Meta 
añadiendo verbose_name, verbose_name_plural y ordering para ordenar por el campo especificado:

<pre><code>
class Project(models.Model):
    
	title = models.CharField(max_length=200)
	......
	......
	
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] # Ordenar por creación. Si se pone el - delante, ordena del mas nuevo al más antiguo
</code></pre>

#### Cambiar el nombre de los registros del modelo

Si se pone por defecto, al añadir registros en el panel de administración saldrán de esta manera: <modelo> object (1) como Project object (1).
Para cambiarlo, se necesita modificar el modelo Project de models.py y modificar la clase añadiendo def __str__(self): return self.title como si fuera
el método toString de una clase en Java.

<pre><code>
class Project(models.Model):
	.....
    def __str__(self):
        return self.title
</code></pre>

#### Personalizar el nombre de los campos del Modelo

Es necesario añadir el tag verbose_name al definir el tipo de dato de los campos del modelo:

<pre><code>
class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")
</code></pre>

#### Mostrar los campos created y updated (solo lectura)

Dirigirse a admin.py y crear una clase ProjectAdmin que herede de ModelAdmin para redefinir el campo readonly_fields.
Después añadir esta clase extendida en el admin.site.register:

<pre><code>
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Project, ProjectAdmin)
</code></pre>

#### Cambiar que al guardar las imagenes se guarden en una carpeta personalizada y no en la carpeta raíz

Django por defecto no maneja el contenido multimedia y cuando se añade una imagen en un registro en el panel de administración, también se añade en el
directorio raíz.

Para esto, hay que crear en el directorio raíz una carpeta llamada <b>"media"</b> para almacenar ahí las imágenes.
Para cambiar la ubicación por defecto, ir al <b>settings.py</b> y añadir estas línes al final que lo que hace es establecer la ruta
para guardar las imágenes.

<pre><code>
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
</code></pre>

Para que la carpeta media se encuentre ordenada, es necesario crear una carpeta para cada modelo. Para que se cree de forma automática cuando
se cree una instancia del modelo, es necesario modificar el campo imagen del modelo con el atributo <b>upload_to='carpeta'</b> indicando el nombre
de la carpeta para este modelo.

<pre><code>
class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título") 
    image = models.ImageField(verbose_name="Imagen",upload_to="projects")
</code></pre>

#### Ver los ficheros media dentro de desarrollo.

Modificar el archivo urls.py. Primero se comprueba si está en modo DEBUG. Si es así, se importa static que permite servir ficheros estáticos.
Despues a urlPatters se concatena con la función static() junto con los enlaces de las variables creadas anteriormente: MEDIA_URL y MEDIA_ROOT

<pre><code>
urlpatterns = [
    path('',views.home,name="home"),
    path('about-me/',views.about,name="about"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('contact/',views.contact,name='contact'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static #static que permite servir ficheros estáticos
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
</code></pre>

### Patrón MVT (Model View Template)

1. Mover el portfolio.html de la app core a la app portfolio
2. En la app portfolio, editar el views.py. Se importa el modelo creado y se llama a la función objects.all para que busque todos los proyectos.

<pre><code>
from .models import Project

def portfolio(request):
    projects = Project.objects.all()
    return render(request,'portfolio/portfolio.html',{"projects":projects})
</code></pre>

3. Cambiar el archivo urls.py del proyecto principal ya que ahora se encuentra en otra carpeta la template y la view.
Para que no haya conflicto de nombres entre las views de las apps es mejor renombrarlas:

....
from core import views as core_views
from portfolio import views as portfolio_views

urlpatterns = [
    path('about-me/',core_views.about,name="about"),
    path('portfolio/',portfolio_views.portfolio,name="portfolio"),
	.....
]

4. Vincular la variable projects a la template con las llaves:

<pre><code>
{% block content %}

{% for project in projects %}
    <!-- Proyecto -->
    <div class="row project">  	
        <div class="col-lg-3 col-md-4 offset-lg-1">
            <img class="img-fluid" src="{{project.image.url}}" alt="">
        </div>
      <div class="col-lg-7 col-md-8">
            <h2 class="section-heading title">{{project.title}}</h2>   
        <p>{{project.description}}</p>
       <!-- <p><a href="http://google.com">Más información</a></p> --> 
        </div>
    </div>
{% endfor %}

{% endblock content %}
</code></pre>

<b>En la template, es necesario poner project.image.url porque así buscara también en todos los directorios anteriores la imagen con esa ruta.</b>

## TemplateTags como filtros

Documentación: https://www.w3schools.com/django/django_tags_filter.php
Algunos ejemplos:

- Mostrar número de palabras de una cadena:<b>{{cadena|wordcount}}</b>

- Nº de elementos de una lista:<b>{{list|length}}</b>

- Transformar una {{cadena}} a un formato especial para que sólo contenga alfanuméricos o guiones:<b>{{cadena|slugify}}</b>

- Transformar una cadena en minúsculas:<b>{{cadena|lower}}</b>

- Acceder al último elemento de la lista:<b>{{list|last}}</b>

- Si tuviéramos una cadena {{titulo}} demasiado larga y quisiéramos recortarla a 20 caracteres porque no tenemos suficiente espacio:<b>{{titulo|truncatechars:"20"}}</b>

- Por último, imagina que tenemos una variable {{respuesta}} de tipo NullBooleanField que puede contener tres valores: True, False o None. ¿Qué filtro utilizaríais para mostrar un "Sí", "No", "No sabe/No contesta" en lugar del valor booleano:<b>{{respuesta|yesno:'Si,No,No Sabe/No contesta'}}</b>