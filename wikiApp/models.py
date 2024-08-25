from django.db import models

class TemaWiki(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField(max_length=512)

    def __str__(self):
        return self.nombre

class ArticuloWiki(models.Model):
    titulo = models.CharField(max_length=128)
    contenido = models.TextField(max_length=1024)
    temaRelacionado = models.ForeignKey(TemaWiki, on_delete=models.CASCADE, related_name='articulos')

    def __str__(self):
        return self.titulo
