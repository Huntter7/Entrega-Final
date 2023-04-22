from django.db import models
from django.contrib.auth.models import User

class Posteo(models.Model):
    titulo_cuerpo_celeste = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)
    encabezado = models.CharField(max_length=150)
    texto_descriptivo = models.CharField(max_length=1000)
    owner = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name='owner')
    imagen = models.ImageField(upload_to='posts', null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add = True) 

    def __str__(self):
        return f"{self.id} -- {self.encabezado}"

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    instagram = models.CharField(max_length=80)
    twitter = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='profiles', null=True, blank=True)
    nombre_completo = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pequeña_introduccion = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.id} -- {self.user} -- {self.nombre_completo}"

class Mensajes(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='destinatario')