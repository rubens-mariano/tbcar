"""tbcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='url_principal'),
    path('cadastrosCliente/', cadastroClientes, name='url_cadastroClientes'),
    path('cadastroVeiculo/', cadastroVeiculos, name='url_cadastroVeiculo'),
    path('listagemCliente/', listaClientes, name='url_listaClientes'),
    path('listagemVeiculo/', listaVeiculo, name='url_listaVeiculo'),
    path('tabela/', tabela, name='url_tabela'),
    path('cadastroTabela/', cadastroTabela, name='url_cadastroTabela'),
    path('altera_cliente/<int:id>/', altera_cliente, name='url_altera_cliente'),
    path('altera_veiculo/<int:id>/', altera_veiculo, name='url_altera_veiculo'),
    path('excluir_cliente/<int:id>/', excluir_cliente, name='url_excluir_cliente'),
    path('excluir_veiculo/<int:id>/', excluir_veiculo, name='url_excluir_veiculo'),
    path('excluir_tabela/<int:id>/', excluir_tabela, name='url_excluir_tabela'),
    path('excluir_marca/<int:id>/', excluir_marca, name='url_excluir_marca'),
    path('excluir_rotativo/<int:id>', excluir_rotativo, name='url_excluir_rotativo'),
    path('altera_tabela/<int:id>/', alterar_tabela, name='url_altera_tabela'),
    path('altera_marca/<int:id>/', alterar_marca, name='url_altera_marca'),
    path('altera_rotativo/<int:id>/', alterar_rotativo, name='url_altera_rotativo'),
    path('altera_mensalista/<int:id>/', alterar_mensalista, name='url_altera_mensalista'),
    path('excluir_mensalista/<int:id>/', excluir_mensalista, name='url_excluir_mensalista'),
    path('listagemMarca/', listaMarca, name='url_listaMarca'),
    path('listagemMensalista/', lista_mensalista, name='url_lista_mensalista'),
    path('listagemRotativo/', listaRotativo, name='url_listaRotativo'),
    path('cadastroMarca/', cadastroMarca, name='url_cadastroMarca'),
    path('cadastrosMensalista/', cadastrosMensalista, name='url_cadastrosMensalista'),
    path('cadastroRotativo/', cadastrosRotativos, name='url_cadastroRotativo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
