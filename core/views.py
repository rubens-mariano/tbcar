from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms import *
from core.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'


def home(request):
    return render(request, 'core/index.html')


# =========== Cadastros ===========

@login_required
def cadastroClientes(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente Cadastrado com sucesso!')
            return redirect('url_listaClientes')
        contexto = {'form': form, 'titulo_pagina': 'Cad_Cliente', 'txt_nome_pagina': 'Cadastro de Cliente'}
        return render(request, 'cadastros/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroVeiculos(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'titulo_pagina': 'Cad_Veiculo', 'txt_nome_pagina': 'Cadastro de Veiculo'}
    return render(request, 'cadastros/cadastro.html', contexto)


@login_required
def cadastroTabela(request):
    if request.user.is_staff:
        form = FormTabela(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')

    contexto = {'form': form, 'titulo_pagina': 'Cad_Tabela', 'txt_nome_pagina': 'Cadastro de Tabela'}
    return render(request, 'cadastros/cadastro.html', contexto)


@login_required
def cadastroMarca(request):
    form = FormMarca(request.POST or None, request.FILES or None)
    if request.user.is_staff:
        if form.is_valid():
            form.save()
            return redirect('url_principal')

    contexto = {'form': form, 'titulo_pagina': 'Cad_Marca', 'txt_nome_pagina': 'Cadastrar Marca'}
    return render(request, 'cadastros/cadastro.html', contexto)


@login_required
def cadastrosMensalista(request):
    form = FormMensalista(request.POST or None, request.FILES or None)
    if request.user.is_staff:
        if form.is_valid():
            form.save()
            return redirect('url_principal')

    contexto = {'form': form, 'titulo_pagina': 'Cad_Mensa', 'txt_nome_pagina': 'Cadastro Mensalidade'}
    return render(request, 'cadastros/cadastro.html', contexto)


@login_required
def cadastrosRotativos(request):
    form = FormRotativo(request.POST or None, request.FILES or None)
    if request.user.is_staff:
        if form.is_valid():
            form.save()
            return redirect('url_principal')

    contexto = {'form': form, 'titulo_pagina': "Cad_Rotativo", 'txt_nome_pagina': 'Cadastros de Rotativos'}
    return render(request, 'cadastros/cadastro-rotativo-dividido.html', contexto)


# =========== Listagem ===========


@login_required
def listaClientes(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Cliente.objects.filter(nome__contains=request.POST['input_pesquisa'])
        else:
            dados = Cliente.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o nome do cliente', 'listagem': True}
        print(contexto)
        return render(request, 'listagem/listagemCliente.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listaVeiculo(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Veiculo.objects.filter(placa__contains=request.POST['input_pesquisa'])
        else:
            dados = Veiculo.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o nome do cliente', 'listagem': True}
        return render(request, 'listagem/listagemVeiculo.html', contexto)
    return render(request, 'aviso.html')


@login_required
def lista_mensalista(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Mensalista.objects.filter(veiculo_id__contains=request.POST['input_pesquisa'])
        else:
            dados = Mensalista.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o nome do cliente', 'listagem': True}
        return render(request, 'listagem/listagemMensalista.html', contexto)
    return render(request, 'aviso.hmtl')


@login_required
def listaRotativo(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Rotativo.objects.filter(veiculo_id__contains=request.POST['input_pesquisa'])
        else:
            dados = Rotativo.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o nome do cliente', 'listagem': True}
        return render(request, 'listagem/listagemRotativos.html', contexto)
    return render(request, 'aviso.hmtl')


@login_required
def listaMarca(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Marca.objects.filter(marca__contains=request.POST['input_pesquisa'])
        else:
            dados = Marca.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o nome do cliente', 'listagem': True}
        return render(request, 'listagem/listagemMarca.html', contexto)


@login_required
def tabela(request):
    if request.user.is_staff:
        dados = Tabela.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o nome do cliente', 'listagem': True}
        return render(request, 'listagem/listagemTabela.html', contexto)
    return render(request, 'aviso.html')


# =========== Alterar ===========


def alterar_marca(request, id):
    obj = Marca.objects.get(id=id)
    form = FormMarca(request.POST or None, request.FILES or None, instance=obj)
    if request.user.is_staff:
        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_listaMarca')

    contexto = {'form': form, 'titulo_pagina': 'alter_Marca', 'txt_nome_pagina': 'Atualização de Marca', 'listagem': True}
    return render(request, 'cadastros/cadastro.html', contexto)


def alterar_tabela(request, id):
    obj = Tabela.objects.get(id=id)
    form = FormTabela(request.POST or None, request.FILES or None, instance=obj)
    if request.user.is_staff:

        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_tabela')

    contexto = {'form': form, 'titulo_pagina': 'Alterar Tabela', 'txt_nome_pagina': 'Alterar Tabela'}
    return render(request, 'cadastros/cadastro.html', contexto)


def alterar_rotativo(request, id):
    obj = Rotativo.objects.get(id=id)
    form = FormRotativo(request.POST or None, request.FILES or None, instance=obj)
    if request.user.is_staff:
        if request.POST:
            if form.is_valid():
                obj.calcula_total()
                form.save()
            return redirect('url_listaRotativo')

    contexto = {'form': form, 'titulo_pagina': 'Alterar_Rotativo', 'txt_nome_pagina': 'Editar Rotativo'}
    return render(request, 'cadastros/cadastro-rotativo-dividido.html', contexto)


@login_required
def alterar_mensalista(request, id):
    obj = Mensalista.objects.get(id=id)
    form = FormMensalista(request.POST or None, request.FILES or None, instance=obj)
    if request.user.is_staff:
        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_lista_mensalista')

    contexto = {'form': form, 'titulo_pagina': 'Alterar_Mensalista', 'txt_nome_pagina': 'Editar Mensalista'}
    return render(request, 'cadastros/cadastro.html', contexto)


def altera_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance=obj)

    if request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados do cliente alterado com sucesso!')
        return redirect('url_listaClientes')

    contexto = {'form': form, 'titulo_pagina': 'Alter_Perfil', 'txt_nome_pagina': 'Atualização de Perfil'}
    return render(request, 'cadastros/cadastro.html', contexto)


def altera_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)

    if request.POST:
        if form.is_valid():
            form.save()
        return redirect('url_altera_veiculo')

    contexto = {'form': form, 'titulo_pagina': 'Alter_veiculo', 'txt_nome_pagina': 'Atualização Veiculo'}
    return render(request, 'cadastros/cadastro.html', contexto)


# =========== Excluir ===========


def excluir_tabela(request, id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id=id)
        if request.POST:
            obj.delete()
            contexto = {'txt_tipo': 'Tabela', 'txt_info': obj.descricao, 'txt_url': '/tabela/'}
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto = {'txt_info': obj.descricao}
            return render(request, 'core/confirma_exclusao.html', contexto)


def excluir_marca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id=id)
        contexto = {'txt_tipo': 'Marca', 'txt_info': obj.marca, 'txt_url': '/listagemMarca'}
        if request.POST:
            obj.delete()
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto.update({'txt_info': obj.marca})
            return render(request, 'core/confirma_exclusao.html', contexto)


def excluir_rotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id=id)
        contexto = {'txt_tipo': 'Rotativo', 'txt_info': obj.veiculo_id, 'txt_url': '/listagemRotativo/'}
        if request.POST:
            obj.delete()
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto.update({'txt_info': obj.veiculo_id})
            return render(request, 'core/confirma_exclusao.html', contexto)


def excluir_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id=id)
        contexto = {'txt_tipo': 'Mensalista', 'txt_info': obj.veiculo_id, 'txt_url': '/listagemMensalista/'}
        if request.POST:
            obj.delete()
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto.update({'txt_info': obj.veiculo_id})
            return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def excluir_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    contexto = {'txt_info': obj.nome, 'txt_url': '/listagemCliente/'}
    if request.POST:
        obj.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        contexto.update({'txt_tipo': 'Cliente'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def excluir_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    contexto = {'txt_info': f'{obj.placa} - {obj.modelo}', 'txt_url': '/listagemVeiculo/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo': 'Veiculo'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)