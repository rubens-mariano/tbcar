from django.contrib import admin
from core.models import Marca, Cliente, Veiculo
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Veiculo)