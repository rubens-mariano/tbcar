from pyexpat import model
from django.db import models
from math import ceil

# Create your models here.

class Tabela(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')

    def __str__(self):
        return f'{self.descricao} - R${self.valor}'

    class Meta:
        verbose_name_plural = 'Descrição'


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereco = models.CharField(max_length=150, verbose_name='Endereço', blank=True, null=True)
    complemento = models.CharField(max_length=100, verbose_name='Complemento', blank=True, null=True)
    bairro = models.CharField(max_length=50, verbose_name='Bairro', blank=True, null=True)
    cidade = models.CharField(max_length=100, verbose_name='Cidade', blank=True, null=True)
    telefone = models.CharField(max_length=20, verbose_name='Telefone', blank=True, null=True)
    email = models.EmailField(verbose_name='E-mail')
    foto = models.ImageField(upload_to='cliente_foto', blank=True, null=True, verbose_name='')

    def __str__(self):
        return self.nome


class Marca(models.Model):
    marca = models.CharField(max_length=30, verbose_name='Marca do carro')
    url = models.URLField(verbose_name='Site', blank=True, null=True)
    logo = models.ImageField(upload_to='marca_logo', blank=True, null=True, verbose_name='')

    def __str__(self):
        return self.marca


class Veiculo(models.Model):
    placa = models.CharField(max_length=8, verbose_name='Placa do veículo')
    modelo = models.CharField(max_length=30, verbose_name='Modelo do veículo', blank=True, null=True)
    cor = models.CharField(max_length=50, verbose_name='Cor do veículo', blank=True, null=True)
    marca_id = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Fabricante')
    ano = models.IntegerField(default=2023, verbose_name="Ano do carro", blank=True, null=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    foto = models.ImageField(upload_to="carro_foto", blank=True, null=True)

    def __str__(self):
        if(self.marca_id):
            return f"PLACA: {self.placa} | MODELO: {self.marca_id}"    
        else:
            return f"PLACA: {self.placa}"

    class Meta:
        verbose_name_plural = 'Veículos'


class Mensalista(models.Model):
    veiculo_id = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veículo')
    tabela_id = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name='Veiculo Valor')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')

    def __str__(self):
        return f'{self.veiculo_id}'

    class Meta:
        verbose_name_plural = 'Mensalistas'


class Rotativo(models.Model):
    veiculo_id = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veiculo')
    tabela_id = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name='Veiculo Valor')
    entrada = models.DateTimeField(auto_now=False, verbose_name='Hora de Entrada')
    saida = models.DateTimeField(auto_now=False, verbose_name='Hora de Saida', blank=True, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor Total', blank=True, null=True)
    pago = models.BooleanField(verbose_name="Pago", default=False)
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')

    def __str__(self):
        return f'{self.veiculo_id} - {self.tabela_id}'

    class Meta:
        verbose_name_plural = 'Rotativos'

    def calcula_total(self):

        if self.saida:
            hora = (self.saida - self.entrada).total_seconds() / 3600
            obj = Tabela.objects.get(id=self.tabela_id.pk)

            if hora <= 0.5:
                self.total = obj.valor / 2
            else:
                self.total = ceil(hora) * obj.valor

            return self.total
        return 0.0
