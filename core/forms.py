from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.forms import *
from core.models import *
from captcha.fields import CaptchaField


class FormCliente(ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = Cliente
        fields = '__all__'


class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class FormMarca(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'


class FormTabela(ModelForm):
    class Meta:
        model = Tabela
        fields = '__all__'


class FormMensalista(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


class FormRotativo(ModelForm):
    class Meta:
        model = Rotativo
        fields = '__all__'

        widgets = {
            'entrada': DateTimePickerInput(options={'format': 'DD/MM/YYYY hh:mm:ss'}),
            'saida': DateTimePickerInput(options={'format': 'DD/MM/YYYY hh:mm:ss'})
        }
