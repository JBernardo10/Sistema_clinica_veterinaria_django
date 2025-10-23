from django.contrib import admin
from .models import Clinica, Cliente, Veterinario, Pagamento, Pedido, Pet, ItemServico, Anexos, Servico

# Register your models here.
admin.site.register(Clinica)
admin.site.register(Cliente)
admin.site.register(Veterinario)
admin.site.register(Pet)
admin.site.register(Servico)
admin.site.register(ItemServico)
admin.site.register(Anexos)
admin.site.register(Pedido)
admin.site.register(Pagamento)