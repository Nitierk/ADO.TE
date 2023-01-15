from ast import Return
from email import message
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os Campos!')
        return render(request, 'cadastro.html')
    if senha != confirmar_senha:
        messages.add_message(request, constants.ERROR, 'Digite duas senhas iguais')
        return render(request, 'cadastro.html')
    try:
        user = User.objects.create_user(
            username = nome,
            email = email,
            password = senha 
        )
        #Mensagem Sucesso
        messages.add_message(request, constants.SUCCESS, 'Usuario criado com sucesso')
        return render(request, 'cadastro.html')
    except:
        #Mensagem Erro
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return render(request, 'cadastro.html')
def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(
            username = nome,
            password = senha,
        )
        print(user)

        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou Senha incorretos!')
            return render(request, 'login.html')    

        return render(request, 'login.html')
