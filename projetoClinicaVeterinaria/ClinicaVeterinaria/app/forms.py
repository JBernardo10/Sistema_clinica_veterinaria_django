from django import forms
from .models import Cliente, Clinica, Veterinario, Pet, Pedido, Pagamento, ItemServico, Servico, Anexos

class CadastroClinica_MF(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = '__all__'
        widgets = {
            "nome" : forms.TextInput(attrs={"class": 'formulario'}),
            "CNPJ" : forms.TextInput(attrs={"class":'formulario'}),
            "endereco" : forms.Textarea(attrs={"class": 'formulario', 'rows': '5'}),
            "telefone" : forms.TextInput(attrs={"class": 'formulario'}),
            "logo" : forms.ClearableFileInput(attrs={"class": 'formulario'}),
        }

class CadastroVeterinario_MF(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = '__all__'
        widgets = {
            "nome" : forms.TextInput(attrs={"class": 'formulario'}),
            "Especialidade" : forms.TextInput(attrs={"class":'formulario'}),
            "telefone" : forms.TextInput(attrs={"class": 'formulario'}),
            "idClinica": forms.Select(attrs={"class": "formulario"}),
        }

class CadastroCliente_MF(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            "nome" : forms.TextInput(attrs={"class": 'formulario'}),
            "telefone" : forms.TextInput(attrs={"class":'formulario'}),
            "email": forms.TextInput(attrs={"class": "formulario", "type": "email"}),
            "endereco": forms.Textarea(attrs={"class": 'formulario', 'rows': '5'}),
            "idClinica": forms.Select(attrs={"class": "formulario"}),
        }


class CadastroPedido_MF(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['dataPedido'] 
        widgets = {
           "dataPedido": forms.DateInput(attrs={"class": "formulario", "type": "date"}),
            "valorTotal": forms.NumberInput(attrs={"class": "formulario","step": "0.01"}),
            "idCliente": forms.Select(attrs={"class": "formulario"}),
            "idVeterinario": forms.Select(attrs={"class": "formulario"}),
            "anexos": forms.CheckboxInput(attrs={"class": "formulario"}),
            "idPet": forms.Select(attrs={"class": "formulario"}),
        }


class CadastroPet_MF(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            "nome": forms.TextInput(attrs={"class": "formulario"}),
            "tipo": forms.TextInput(attrs={"class": "formulario"}),
            "raca": forms.TextInput(attrs={"class": "formulario"}),
            "dataNascimento": forms.DateInput(attrs={"class": "formulario", "type": "date"},  format="%Y-%m-%d"),
            "sexo": forms.TextInput(attrs={"class": "formulario"}),
            "idDono": forms.Select(attrs={"class": "formulario"}),
            "imagemPet": forms.ClearableFileInput(attrs={"class": "formulario"}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Isso garante que o Django interprete e exiba a data no formato correto
            self.fields["dataNascimento"].input_formats = ["%Y-%m-%d"]


class CadastroServico_MF(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            "dataServico": forms.DateTimeInput(attrs={
                "class": "formulario",
                "type": "datetime-local"
            }),
            "tipo": forms.TextInput(attrs={"class": "formulario"}),
            "descricao": forms.Textarea(attrs={"class": "formulario"}),
            "valor":  forms.NumberInput(attrs={"class": "formulario","step": "0.01","placeholder": "R$ 0,00"}),
        }


class CadastroAnexos_MF(forms.ModelForm):
    class Meta:
        model = Anexos
        fields = '__all__'
        widgets = {
            "duracao": forms.TextInput(attrs={"class": "formulario"}),
            "informacoes": forms.Textarea(attrs={"class": "formulario", 'rows': '5'}),
            "idServico": forms.Select(attrs={"class": "formulario"}),
        }

class CadastroItemServico_MF(forms.ModelForm):
    class Meta:
        model = ItemServico
        fields = '__all__'
        widgets = {
            "qtd": forms.NumberInput(attrs={"class": "formulario", "min": "1"}),
            "subTotal": forms.NumberInput(attrs={"class": "formulario", "step": "0.01"}),
            "idServico": forms.Select(attrs={"class": "formulario"}),
            "idPedido": forms.Select(attrs={"class": "formulario"}),
        }

class CadastroPagamento_MF(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'
        widgets = {
            "valor": forms.NumberInput(attrs={"class": "formulario","step": "0.01","placeholder": "R$ 0,00"}),
            "formaPagamento": forms.TextInput(attrs={"class": "formulario"}),
            "idPedido": forms.Select(attrs={"class": "formulario"}),
        }