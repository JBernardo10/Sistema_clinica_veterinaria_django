from django.db import models
from django.utils import timezone
from django.db.models import Sum


# Create your models here.
class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=20, unique=True)
    endereco = models.TextField()
    telefone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    
    def __str__(self):
        return self.nome


class Veterinario(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    idClinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome
 

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    endereco = models.TextField()
    idClinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


class Pet(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    raca = models.CharField(max_length=50, blank=True)
    dataNascimento = models.DateField(auto_now=False, auto_now_add=False)
    sexo = models.CharField(max_length=50)
    idDono = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    imagemPet = models.ImageField(upload_to='imagemPet', null=True, blank=True)

    def __str__(self):
        return self.nome
    

class Servico(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Ser. {self.id} - {self.tipo}'


class Pedido(models.Model):
    dataPedido = models.DateTimeField(auto_now_add=True)
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    idCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    idPet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    idVeterinario = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True)
    anexos = models.BooleanField(null=True)

    def __str__(self):
        return f'Ped. {self.id} - Cli. {self.idCliente}'


class Anexos(models.Model):
    duracao = models.CharField(max_length=50)
    informacoes = models.TextField()
    idServico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Anex. {self.id} - Serv. {self.idServico}'

class ItemServico(models.Model):
    qtd = models.IntegerField(default=1)
    subTotal = models.DecimalField(max_digits=10, decimal_places=2)
    idServico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.idServico and self.qtd:
            self.subTotal = self.idServico.valor * self.qtd
        super().save(*args, **kwargs)
    
      # Atualiza o total do pedido
        if self.idPedido:
            total = ItemServico.objects.filter(idPedido=self.idPedido).aggregate(Sum('subTotal'))['subTotal__sum'] or 0
            self.idPedido.valorTotal = total
            self.idPedido.save(update_fields=['valorTotal'])

    def delete(self, *args, **kwargs):
        pedido = self.idPedido
        super().delete(*args, **kwargs)
        if pedido:
            total = ItemServico.objects.filter(idPedido=pedido).aggregate(Sum('subTotal'))['subTotal__sum'] or 0
            pedido.valorTotal = total
            pedido.save(update_fields=['valorTotal'])

    def __str__(self):
        return f'Item {self.id} - Ped. {self.idPedido}'

class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    formaPagamento = models.CharField(max_length=50)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pag. {self.id} - Ped. {self.idPedido}'