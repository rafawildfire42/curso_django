from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                           .filter(status='publicado')
    #classe para gerenciar os posts publicados

class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )

    titulo = models.CharField(max_length=250)
    slug   = models.SlugField(max_length=250)
    autor  = models.ForeignKey(User, on_delete = models.CASCADE)
    conteudo = models.TextField()

    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices = STATUS, default = "rascunhos")

    objects   = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        #return reverse('post_detail', args = [self.pk])
        return reverse('post_detail', args = [self.slug])

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo


# Create your models here.
"""
Post.objects.bulk_create([
    Post(titulo='Testando o shell do Django 1', slug='testando-o-shell-do-django-1', conteudo='ola mundo 1', autor=user),
    Post(titulo='Testando o shell do Django 2', slug='testando-o-shell-do-django-2', conteudo='ola mundo 2', autor=user),
    Post(titulo='Testando o shell do Django 3', slug='testando-o-shell-do-django-3', conteudo='ola mundo 3', autor=user)
)]
"""