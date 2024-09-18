from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ProdutoCadastroModel, Categoria
from .forms import ProdutoCadastroForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth


# Landing page site-cardápio
def index(request):
    return render(request, "site_rafaburguer/index.html")


# Index administrador
@login_required(login_url="site_rafaburguer:tela_login")
def index_administrador(request):
    username = request.user.username
    return render(request, "global/index_administrador.html", {"username": username})


# Login/logout
def login_view(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Logado com sucesso")
            return redirect("site_rafaburguer:index_administrador")
        messages.error(request, "Login inválido")
    return render(request, "global/tela_login.html", {"form": form})


@login_required(login_url="site_rafaburguer:tela_login")
def logout_view(request):
    auth.logout(request)
    return redirect("site_rafaburguer:tela_login")


@login_required(login_url="site_rafaburguer:tela_login")
def listar_produtos(request):
    username = request.user.username  # Obtém o nome de usuário do request
    produtos = ProdutoCadastroModel.objects.all()
    categorias = Categoria.objects.all()

    query_nome = request.GET.get("nome")
    query_categoria_id = request.GET.get("categoria")
    query_categoria_nome = None

    if query_categoria_id:
        try:
            categoria = Categoria.objects.get(id=query_categoria_id)
            query_categoria_nome = categoria.name
            produtos = produtos.filter(categoria__id=query_categoria_id)
        except Categoria.DoesNotExist:
            query_categoria_id = None

    if query_nome:
        produtos = produtos.filter(nome_do_produto__icontains=query_nome)

    produtos = produtos.order_by("-data_de_criação")

    return render(
        request,
        "global/partials/_listar_produtos.html",
        {
            "produtos": produtos,
            "categorias": categorias,
            "username": username,
            "query_nome": query_nome,
            "query_categoria": query_categoria_nome,
        },
    )


@login_required(login_url="site_rafaburguer:tela_login")
def adicionar_produto(request):
    username = request.user.username  # Obtém o nome de usuário do request
    if request.method == "POST":
        form = ProdutoCadastroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto adicionado com sucesso!")
            return redirect("site_rafaburguer:listar_produtos")
    else:
        form = ProdutoCadastroForm()
    return render(
        request,
        "global/partials/_adicionar_produto.html",
        {"form": form, "username": username},
    )


@login_required(login_url="site_rafaburguer:tela_login")
def atualizar_produto(request, id):
    username = request.user.username  # Obtém o nome de usuário do request
    produto = get_object_or_404(ProdutoCadastroModel, id=id)
    if request.method == "POST":
        form = ProdutoCadastroForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Produto {produto.nome_do_produto} atualizado com sucesso!"
            )
            return redirect("site_rafaburguer:listar_produtos")
    else:
        form = ProdutoCadastroForm(instance=produto)
    return render(
        request,
        "global/partials/_atualizar_produto.html",
        {"form": form, "produto": produto, "username": username},
    )


@login_required(login_url="site_rafaburguer:tela_login")
def excluir_produto(request, id):
    username = request.user.username  # Obtém o nome de usuário do request
    produto = get_object_or_404(ProdutoCadastroModel, id=id)
    if request.method == "POST":
        produto.delete()
        messages.success(
            request, f"Produto {produto.nome_do_produto} deletado com sucesso!"
        )
        return redirect("site_rafaburguer:listar_produtos")
    return render(
        request,
        "global/partials/_excluir_produto.html",
        {"produto": produto, "username": username},
    )
