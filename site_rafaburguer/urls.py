from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from site_rafaburguer import views

app_name = "site_rafaburguer"

urlpatterns = [
    # LANDING PAGE
    path("", views.index, name="index"),
    # Administrador Rafa burg's
    path("administrador/index/", views.index_administrador, name="index_administrador"),
    # LOGIN/LOGOUT
    path("login/", views.login_view, name="tela_login"),
    path("logout/", views.logout_view, name="tela_logout"),
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


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
