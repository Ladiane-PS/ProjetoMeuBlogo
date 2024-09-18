
from django.db import models  # Importa o módulo models do Django, necessário para definir os modelos (tabelas do banco de dados)
 
# blog/models.py
class Post(models.Model):  # Define a classe Post, que representa um modelo (tabela) no banco de dados
    titulo = models.CharField(max_length=200)  # Campo de texto com um limite máximo de 200 caracteres para o título do post
    conteudo = models.TextField()  # Campo de texto sem limite de caracteres para o conteúdo do post
    data_publicacao = models.DateTimeField(auto_now_add=True)  # Armazena a data e a hora em que o post foi criado, preenchido automaticamente
    imagem_destacada = models.ImageField(upload_to='images/', blank=True, null=True)  # Campo de upload de imagem, opcional (pode ser em branco ou nulo) e salvo no diretório 'images/'


# Model (M): A camada "Model" é representada pelo arquivo models.py, que define a estrutura dos dados. No seu caso, no diretório meublog/blog, o arquivo models.py contém a classe Post,
# que define os campos de um post no blog, como titulo, conteudo, data_publicacao, e imagem_destaque.