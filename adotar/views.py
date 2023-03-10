from datetime import datetime
from django.shortcuts import render, redirect
from adotar.models import PedidoAdocao
from divulgar.models import Pet, Raca
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.core.mail import send_mail

def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status="P")
        racas = Raca.objects.all()
        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')

        if cidade:
            pets = pets.filter(cidade__icontains=cidade)
        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)
        return render(request, 'listar_pets.html', {'pets':pets, 'racas':racas, 'cidade':cidade,'raca_filter':raca_filter})
def pedido_adocao(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status='P')

    if not pet.exists():
        messages.add_message(redirect, constants.WARNING, 'Pet já adotado!')
        return redirect('/adotar')

    pedido = PedidoAdocao(pet=pet.first(),
                            usuario=request.user,
                            data= datetime.now())
    pedido.save()
    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
    return redirect('/adotar')
def processa_pedido_adocao(request, id_pedido):
    status = request.GET.get('status')
    pedido = PedidoAdocao.objects.get(id=id_pedido)
    pet = Pet.objects.get(id=pedido.pet.id)
    if status == "A":
        pedido.status = "AP"
        pet.status = 'A' 
        string = '''Olá, sua adoção foi aprovada com sucesso'''
    elif status == "R":
        pedido.status = "R"
        pet.status = 'P' 
        string = '''Olá, sua adoção foi recusada'''

    print(f"Status do pet: {pet.status}")
    pet.save()
    pedido.save()

    email = send_mail(
        'Sua adoção foi processada',
        string,
        'kaukau007500@gmail.com',
        [pedido.usuario.email,]        
    )

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção processado')

    return redirect('/divulgar/ver_pedido_adocao')
    
