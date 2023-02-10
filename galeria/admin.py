from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada",)#visualizacao do banco de dados
    list_display_links = ("id", "nome",)#colocar como parametro de links
    search_fields = ("nome",)#adicionar "pesquisar" no django admin
    list_filter = ("categoria","usuarios",)#filtrar pesquisa por categorias
    list_editable = ("publicada",)
    list_per_page = 10#limitar tamanho de itens por pagina

admin.site.register(Fotografia, ListandoFotografia)