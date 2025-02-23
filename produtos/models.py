from django.db import models

# Create your models here.
class Produto(models.Model):
    CATEGORIAS = [
        ('cursos', 'Cursos'),
        ('ebook', 'E-books'),
        ('cabelo', 'Cabelo'),
        ('roupa', 'Roupa'),
        ('tenis', 'Tênis'),
        ('livros', 'Livros'),
        ('diversos', 'Diversos'),
    ]

    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    link_afiliado = models.URLField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

def __str__(self):
    return self.nome