from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Cliente, Ordem
from .forms import Buscacliente, Clienteform, Atualizacliente, Ordemform, Buscaordem, Atualizaordem

########################################### USUARIO(RETIFICAS) #############################################

def cadastrarusuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('user')
        mail = request.POST.get('email')
        senha = request.POST.get('password')
        
        if User.objects.filter(username = usuario).exists():
            return messages.error(request, 'Erro! Usuário já existe')
        elif User.objects.filter(email = mail).exists():
            return messages.error(request, 'Erro! Já existe um usuário com o mesmo e-mail')
            
        newuser = User.objects.create_user(username=usuario, email=mail, password=senha)
        newuser.save()
        messages.success(request, 'Registrado com sucesso!')
        return redirect('home')
    return render(request,'registro.html')

def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('user')
        senha = request.POST.get('password')

        user = authenticate(username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('listaordem')
        else:
            messages.error(request, 'Erro! Usuario ou senha inválidos')
    else:
        logout(request)
    return render(request,'login.html')

def sair(request):
    if request.user.is_authenticated and request.method == 'POST' and request.GET.get('logout'):
        return redirect('home')

########################################### CLIENTES #############################################

def cadastrocliente(request):
    if request.user.is_authenticated:
        form = Clienteform(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            messages.success(request, 'Cliente cadastrado!')
            return redirect('/cliente')
        context = { "form": form }
        return render(request,'cadastrocliente.html', context)
    else: return redirect('home')

def listacliente(request):
    if not request.user.is_authenticated:
        return redirect('home')
        
    busca = request.POST.get('campobusca')
    queryset = Cliente.objects.filter(usuario=request.user.id)
    #form = Buscacliente(request.POST or None)

    if request.method == "POST":
        if request.GET.get('buscacpf'):
            queryset = Cliente.objects.filter(cpf=busca, usuario=request.user.id)
        elif request.GET.get('buscacnpj'):
            queryset = Cliente.objects.filter(cnpj=busca, usuario=request.user.id)

    context = {
        "queryset": queryset,
    }
    return render(request, 'cliente.html', context)

def atualizacliente(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')

    queryset = Cliente.objects.get(id=pk)
    form = Atualizacliente(instance=queryset)
    if request.method == 'POST':
        form = Atualizacliente(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect ('/cliente')
    context = {
        "form": form,
    }
    return render (request, 'cadastrocliente.html', context)

def apagarcliente(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')

    queryset = Cliente.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/cliente')
    return render(request, 'apagarcliente.html')

########################################### ORDENS DE SERVIÇO #############################################

def novaordem(request):
    if not request.user.is_authenticated:
        return redirect('home')

    form = Ordemform(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        obj = form.save(commit=False)
        obj.usuario = request.user
        obj.save()
        messages.success(request, 'Ordem de serviço criada!')
        return redirect('listaordem')
    context = {
        "form": form,
    }
    return render(request,'novaordem.html')

def listaordem(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    busca = request.POST.get('campobusca')
    queryset = Ordem.objects.filter(usuario=request.user.id)

    if request.method == "POST":
        if request.GET.get('buscaordem'):
            queryset = Ordem.objects.filter(id=busca, usuario=request.user.id)
        elif request.GET.get('buscaordemcliente'):
            queryset = Ordem.objects.filter(cliente=busca, usuario=request.user.id)

    context = {
        "queryset": queryset,
    }
    return render(request, 'index.html', context)

def atualizaordem(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')

    queryset = Ordem.objects.get(id=pk)
    form = Atualizaordem(instance=queryset)
    if request.method == 'POST':
        form = Atualizaordem(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect ('listaordem')
    context = {
        "form": form,
    }
    return render (request, 'novaordem.html', context)

def apagarordem(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')

    queryset = Ordem.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('listaordem')
    return render(request, 'apagarordem.html')
