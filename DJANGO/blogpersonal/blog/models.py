from django.db import models
# Ck Editor
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    imagen = models.ImageField(verbose_name='Imágen', upload_to='blog')
    title = models.CharField(max_length=100, verbose_name='Título')
    desc = models.TextField(verbose_name= 'Descripción')
    content = RichTextField(verbose_name='Contenido')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']


    def __str__(self):
        return self.title
