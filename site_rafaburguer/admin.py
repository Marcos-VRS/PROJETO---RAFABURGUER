from django.contrib import admin
from .models import ProdutoCadastroModel, Categoria


# Registro do modelo Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Corrigido para uma tupla
    search_fields = ("name",)  # Corrigido para uma tupla


# Registro do modelo ProdutoCadastroModel
@admin.register(ProdutoCadastroModel)
class ProdutoCadastroModelAdmin(admin.ModelAdmin):
    list_display = (
        "nome_do_produto",
        "preço",
        "descrição",
        "categoria",
        "data_de_criação",
    )
    search_fields = ("nome_do_produto", "categoria__nome")
