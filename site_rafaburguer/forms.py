from django import forms
from .models import ProdutoCadastroModel


class ProdutoCadastroForm(forms.ModelForm):
    class Meta:
        model = ProdutoCadastroModel
        fields = [
            "categoria",
            "nome_do_produto",
            "foto_do_produto",
            "descrição",
            "preço",
        ]
