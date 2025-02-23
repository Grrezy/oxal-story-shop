from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import ProdutoForm, RegistroForm
from .models import Produto




# Create your views here.









# Página de Login
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Agora redireciona corretamente para o painel
        else:
            return render(request, 'auth/login.html', {'error': 'Credenciais inválidas'})

    return render(request, 'auth/login.html')


def logout_view(request):
   logout(request)
   return redirect('login_view')

def registro_view(request):
    return render(request, 'auth/registro.html')





# Verifica se o usuário é administrador
def is_admin(user):
    return user.is_superuser or user.groups.filter(name="Gerentes").exists()




@login_required
def dashboard(request):
    return render(request, 'auth/dashboard.html')

def lista_produtos(request, categoria=None):
    query = request.GET.get('q')
    produtos = Produto.objects.all()
    
    if categoria:
        produtos = produtos.filter(categoria=categoria)
    
    if query:
        produtos = produtos.filter(nome__icontains=query)

    pode_adicionar = request.user.is_authenticated and (request.user.is_superuser or request.user.groups.filter(name="Gerentes").exists())

    

    return render(request, "produtos/lista_produtos.html", {"produtos": produtos, "pode_adicionar": pode_adicionar})

def is_admin(user):
    return user.is_superuser or user.groups.filter(name="Gerentes").exists()

    

#adicionar produtos
@login_required(login_url="login")
@user_passes_test(is_admin)
@login_required
def adicionar_produto(request):
     if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Agora redireciona corretamente para o painel do usuário
        else:
            form = ProdutoForm()

        return render(request, 'produtos/adicionar_produto.html', {'form': form})


def detalhes_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})


