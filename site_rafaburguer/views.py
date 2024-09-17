from django.shortcuts import render, get_object_or_404, redirect
from .models import ProdutoCadastroModel
from .forms import ProdutoCadastroForm
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "site_rafaburguer/index.html")


# Listar produtos
def listar_produtos(request):
    produtos = ProdutoCadastroModel.objects.all()
    return render(
        request, "global/partials/_listar_produtos.html", {"produtos": produtos}
    )


# Adicionar produto
def adicionar_produto(request):
    if request.method == "POST":
        form = ProdutoCadastroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("site_rafaburguer:listar_produtos")
    else:
        form = ProdutoCadastroForm()
    return render(request, "global/partials/_adicionar_produto.html", {"form": form})


# Atualizar produto
def atualizar_produto(request, id):
    produto = get_object_or_404(ProdutoCadastroModel, id=id)
    if request.method == "POST":
        form = ProdutoCadastroForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("site_rafaburguer:listar_produtos")
    else:
        form = ProdutoCadastroForm(instance=produto)
    return render(
        request,
        "global/partials/_atualizar_produto.html",
        {"form": form, "produto": produto},
    )


# Excluir produto
def excluir_produto(request, id):
    produto = get_object_or_404(ProdutoCadastroModel, id=id)
    if request.method == "POST":
        produto.delete()
        return redirect("site_rafaburguer:listar_produtos")
    return render(
        request, "global/partials/_excluir_produto.html", {"produto": produto}
    )
