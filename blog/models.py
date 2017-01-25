#encoding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=250)

    created_at = models.DateField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Post(models.Model):
    title = models.CharField('Título', max_length=250)
    description = models.TextField('Descrição')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField('Identificador', max_length=250)
    image = models.CharField('Imagem', max_length=1000)

    created_at = models.DateField('Criado em', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'