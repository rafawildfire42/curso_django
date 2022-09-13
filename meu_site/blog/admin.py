from django.contrib import admin
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'autor', 'publicado', 'status')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    date_hierarchy = 'publicado'
    raw_id_fields = ('autor',)
    prepopulated_fields = {'slug': ('titulo',)}
# Register your models here.
