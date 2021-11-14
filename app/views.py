from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Cliente, Ordem
from .forms import Buscacliente, Clienteform, Atualizacliente, Ordemform, Buscaordem, Atualizaordem
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name = 'login.html'

class RegisterView(CreateView):
    #model = Cliente
    #fields = ['nome', 'cpf', 'cnpj', 'endereco', 'bairro', 'cidade', 'estado', 'cep', 'telefone']
    #template_name = 'cadastros/form.html'
    #sucess_url = reverse_lazy('home')
    template_name = 'registro.html'
    
def ordemservico(request):
    if(request.user.is_authenticated):
        return render(request,'login.html')

    form = Ordemform(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/ordemservico')
    context = {
        "form": form,
    }
    return render(request,'index.html', context)

def cadastrocliente(request):
    if(request.user.is_authenticated):
        return render(request,'login.html')

    form = Clienteform(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Cliente cadastrado!')
        return redirect('/cliente')
    context = {
        "form": form,
    }
    return render(request,'cadastrocliente.html', context)

def novaordem(request):
    if(request.user.is_authenticated):
        return render(request,'login.html')

    form = Ordemform(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Cliente cadastrado!')
        return redirect('/')
    context = {
        "form": form,
    }
    return render(request,'novaordem.html', context)

def listacliente(request):
    if(request.user.is_authenticated):
        return render(request,'login.html')

    queryset = Cliente.objects.all()
    form = Buscacliente(request.POST or None)
    if request.method == 'POST':
        queryset = Cliente.objects.filter(cpf__icontains=form['cpf'].value(), usuario=request.user.id)
    context = {
        "form": form,
        "queryset": queryset,
    }
    return render(request, 'cliente.html', context)

def listaordem(request):
    if(request.user.is_authenticated):
        return render(request,'login.html')
        
    queryset = Ordem.objects.all()
    form = Buscaordem(request.POST or None)
    if request.method == 'POST':
        queryset = Ordem.objects.filter(numeroordem__icontains=form['numeroordem'].value(), usuario=request.user.id)
    context = {
        "form": form,
        "queryset": queryset,
    }
    return render(request, 'index.html', context)

def atualizacliente(request, pk):
    if(request.user.is_authenticated):
        return render(request,'login.html')

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

def atualizaordem(request, pk):
    if(request.user.is_authenticated):
        return render(request,'login.html')

    queryset = Ordem.objects.get(id=pk)
    form = Atualizaordem(instance=queryset)
    if request.method == 'POST':
        form = Atualizaordem(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect ('/')
    context = {
        "form": form,
    }
    return render (request, 'novaordem.html', context)

def apagarordem(request, pk):
    if(request.user.is_authenticated):
        return render(request,'login.html')

    queryset = Ordem.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/')
    return render(request, 'apagarordem.html')

def apagarcliente(request, pk):
    if(request.user.is_authenticated):
        return render(request,'login.html')

    queryset = Cliente.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/cliente')
    return render(request, 'apagarcliente.html')