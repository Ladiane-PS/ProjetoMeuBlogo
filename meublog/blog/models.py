
from django.db import models

# blog/models.py
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem_destacada = models.ImageField(upload_to='images/', blank=True, null=True)

