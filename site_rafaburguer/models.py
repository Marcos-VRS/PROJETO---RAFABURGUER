from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class ProdutoCadastroModel(models.Model):
    class Meta:
        verbose_name = "Cadastro de produtos"
        verbose_name_plural = "Cadastro de produtos"

    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, blank=True, null=True
    )
    nome_do_produto = models.CharField(max_length=50)
    foto_do_produto = models.ImageField(blank=True, upload_to="pictures/%Y/%m")

    descrição = models.TextField()
    preço = models.CharField(max_length=50)
    data_de_criação = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.nome_do_produto}"
