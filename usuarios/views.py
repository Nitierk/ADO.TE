from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        return HttpResponse("Teste")