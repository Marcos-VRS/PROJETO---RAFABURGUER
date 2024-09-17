from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from site_rafaburguer import views

app_name = "site_rafaburguer"

urlpatterns = [
    # LANDING PAGE
    path("", views.index, name="index"),
    # CRUD DOS PRODUTOS
    path("produtos/", views.listar_produtos, name="listar_produtos"),
    path("produtos/adicionar/", views.adicionar_produto, name="adicionar_produto"),
    path(
        "produtos/atualizar/<int:id>/",
        views.atualizar_produto,
        name="atualizar_produto",
    ),
    path("produtos/excluir/<int:id>/", views.excluir_produto, name="excluir_produto"),
]
