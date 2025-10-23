from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Clinica, Veterinario, Pet, Pedido, Pagamento, ItemServico, Servico, Anexos
from .forms import CadastroClinica_MF, CadastroVeterinario_MF, CadastroCliente_MF, CadastroServico_MF, CadastroAnexos_MF, CadastroItemServico_MF, CadastroPagamento_MF, CadastroPedido_MF, CadastroPet_MF
from django.core.paginator import Paginator
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def base(request):
    return render(request, 'base.html')

@login_required
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def clinica(request):
    clinicas = Clinica.objects.all()
    pc = request.GET.get('pc',1)
    listaClinicas = Paginator(clinicas, 3).get_page(pc)

    formulario = CadastroClinica_MF(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("clinica")
    return render(request, 'clinica/clinica.html',{
        "clinicas": listaClinicas, "formulario": formulario
    })
def editarClinica(request, id):
    clinicaEditar = get_object_or_404(Clinica, pk=id)
    formulario = CadastroClinica_MF(request.POST or None, instance=clinicaEditar)
    if formulario.is_valid():
        formulario.save()
        return redirect('clinica')
    
    return render(request, 'clinica/editarClinica.html', {"formulario": formulario, "clinica": clinicaEditar})
def excluirClinica (request, id):
    clinicaExcluir = get_object_or_404(Clinica, pk=id)
    if request.method == 'POST':
        clinicaExcluir.delete()
        return redirect('clinica')
    
    return render(request, 'clinica/excluirClinica.html', {"clinica": clinicaExcluir})

@login_required
def cliente(request):
    clientes = Cliente.objects.all()
    pc = request.GET.get('pc',1)
    listaClientes = Paginator(clientes, 3).get_page(pc)

    formulario = CadastroCliente_MF
    if request.method == 'POST':
        formulario = CadastroCliente_MF(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("cliente")
    return render(request, 'cliente/cliente.html',{
        "clientes": listaClientes, "formulario": formulario
    })
def editarCliente(request, id):
    clienteEditar = get_object_or_404(Cliente, pk=id)
    formulario = CadastroCliente_MF(request.POST or None, instance=clienteEditar)
    if formulario.is_valid():
        formulario.save()
        return redirect('cliente')
    return render(request, 'cliente/editarCliente.html', {"formulario": formulario, "cliente": clienteEditar})
def excluirCliente(request, id):
    clienteExcluir = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        clienteExcluir.delete()
        return redirect('cliente')
    
    return render(request, 'cliente/excluirCliente.html', {"cliente": clienteExcluir})

@login_required
def veterinario(request):
    veterinario = Veterinario.objects.all()
    pc = request.GET.get('pc',1)
    listaVeterinarios = Paginator(veterinario, 3).get_page(pc)

    formulario = CadastroVeterinario_MF
    if request.method == 'POST':
        formulario = CadastroVeterinario_MF(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("veterinario")
    return render(request, 'veterinario/veterinario.html',{
        "veterinarios": listaVeterinarios, "formulario": formulario
    })
def editarVeterinario(request, id):
    veterinarioEditar = get_object_or_404(Veterinario, pk=id)
    formulario = CadastroVeterinario_MF(request.POST or None, instance=veterinarioEditar)
    if formulario.is_valid():
        formulario.save()
        return redirect('veterinario')  # volta pra lista de veterinários
    return render(request, 'veterinario/editarVeterinario.html', {
        "formulario": formulario,"veterinario": veterinarioEditar
    })
def excluirVeterinario(request, id):
    veterinarioExcluir = get_object_or_404(Veterinario, pk=id)
    if request.method == 'POST':
        veterinarioExcluir.delete()
        return redirect('veterinario')
    
    return render(request, 'veterinario/excluirVeterinario.html', {
        "veterinario": veterinarioExcluir
    })

@login_required
def pedido(request):
    pedidos = Pedido.objects.all()
    pc = request.GET.get('pc',1)
    listaPedidos = Paginator(pedidos, 3).get_page(pc)

    formulario = CadastroPedido_MF
    if request.method == 'POST':
        formulario = CadastroPedido_MF(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("pedido")
    return render(request, 'pedido/pedido.html',{
        "pedidos": listaPedidos, "formulario": formulario
    })
def editarPedido(request, id):
    pedidoEditar = get_object_or_404(Pedido, pk=id)
    formulario = CadastroPedido_MF(request.POST or None, instance=pedidoEditar)
    if formulario.is_valid():
        formulario.save()
        return redirect('pedido')
    return render(request, 'pedido/editarPedido.html', {
        "formulario": formulario,"pedido": pedidoEditar
    })
def excluirPedido(request, id):
    pedidoExcluir = get_object_or_404(Pedido, pk=id)
    if request.method == 'POST':
        pedidoExcluir.delete()
        return redirect('pedido')
    
    return render(request, 'pedido/excluirPedido.html', {
        "pedido": pedidoExcluir
    })

@login_required
def servico(request):
    servicos = Servico.objects.all()
    pc = request.GET.get('pc', 1)
    listaServicos = Paginator(servicos, 3).get_page(pc)

    formulario = CadastroServico_MF()
    if request.method == 'POST':
        formulario = CadastroServico_MF(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('servico')

    return render(request, 'servico/servico.html', {
        "servicos": listaServicos,
        "formulario": formulario
    })
def editarServico(request, id):
    servicoEditar = get_object_or_404(Servico, pk=id)
    formulario = CadastroServico_MF(request.POST or None, instance=servicoEditar)

    if formulario.is_valid():
        formulario.save()
        return redirect('servico')

    return render(request, 'servico/editarServico.html', {
        "formulario": formulario,
        "servico": servicoEditar
    })
def excluirServico(request, id):
    servicoExcluir = get_object_or_404(Servico, pk=id)

    if request.method == 'POST':
        servicoExcluir.delete()
        return redirect('servico')

    return render(request, 'servico/excluirServico.html', {
        "servico": servicoExcluir
    })

@login_required
def pagamento(request):
    pagamentos = Pagamento.objects.all().order_by('-id')
    pc = request.GET.get('pc', 1)
    listaPagamentos = Paginator(pagamentos, 5).get_page(pc)

    formulario = CadastroPagamento_MF(request.POST or None)

   
    pedidos_abertos = []
    for pedido in Pedido.objects.all():
        total_pago = Pagamento.objects.filter(idPedido=pedido).aggregate(Sum('valor'))['valor__sum'] or 0
        if total_pago < pedido.valorTotal:
            pedidos_abertos.append(pedido)

    
    formulario.fields['idPedido'].queryset = Pedido.objects.filter(id__in=[p.id for p in pedidos_abertos])

    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('pagamento')

    return render(request, 'pagamento/pagamento.html', {
        "pagamentos": listaPagamentos,
        "formulario": formulario,
        "pedidos_abertos": pedidos_abertos,  # usaremos no JS
    })
def editarPagamento(request, id):
    pagamentoEditar = get_object_or_404(Pagamento, pk=id)
    formulario = CadastroPagamento_MF(request.POST or None, instance=pagamentoEditar)

    if formulario.is_valid():
        formulario.save()
        return redirect('pagamento')

    return render(request, 'pagamento/editarPagamento.html', {
        "formulario": formulario,
        "pagamento": pagamentoEditar
    })
def excluirPagamento(request, id):
    pagamentoExcluir = get_object_or_404(Pagamento, pk=id)

    if request.method == 'POST':
        pagamentoExcluir.delete()
        return redirect('pagamento')

    return render(request, 'pagamento/excluirPagamento.html', {
        "pagamento": pagamentoExcluir
    })

@login_required
def pet(request):
    pets = Pet.objects.all()
    pc = request.GET.get('pc', 1)
    listaPets = Paginator(pets, 3).get_page(pc)

    formulario = CadastroPet_MF
    if request.method == 'POST':
        formulario = CadastroPet_MF(request.POST, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('pet')

    return render(request, 'pet/pet.html', {
        "pets": listaPets,
        "formulario": formulario
    })
def editarPet(request, id):
    petEditar = get_object_or_404(Pet, pk=id)
    formulario = CadastroPet_MF(request.POST or None, request.FILES or None, instance=petEditar,)

    if formulario.is_valid():
        formulario.save()
        return redirect('pet')

    return render(request, 'pet/editarPet.html', {
        "formulario": formulario,
        "pet": petEditar
    })
def excluirPet(request, id):
    petExcluir = get_object_or_404(Pet, pk=id)

    if request.method == 'POST':
        petExcluir.delete()
        return redirect('pet')

    return render(request, 'pet/excluirPet.html', {
        "pet": petExcluir
    })

@login_required
def itemServico(request):
    # --- Lista paginada de itens ---
    itens = ItemServico.objects.all().order_by('-id')
    pc = request.GET.get('pc', 1)
    listaItens = Paginator(itens, 3).get_page(pc)

    # --- Cria o formulário (sempre) ---
    formulario = CadastroItemServico_MF(request.POST or None)

    # --- Pega a lista de serviços (para o JS) ---
    servicos = formulario.fields['idServico'].queryset

    # --- Se o formulário foi enviado e é válido ---
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('itemServico')

    # --- Renderiza a página ---
    return render(request, 'itemServico/itemServico.html', {
        "itens": listaItens,
        "formulario": formulario,
        "servicos": servicos,
    })
def editarItemServico(request, id):
    itemEditar = get_object_or_404(ItemServico, pk=id)
    formulario = CadastroItemServico_MF(request.POST or None, instance=itemEditar)

    if formulario.is_valid():
        formulario.save()
        return redirect('itemServico')

    return render(request, 'itemServico/editarItemServico.html', {
        "formulario": formulario,
        "item": itemEditar
    })
def excluirItemServico(request, id):
    itemExcluir = get_object_or_404(ItemServico, pk=id)

    if request.method == 'POST':
        itemExcluir.delete()
        return redirect('itemServico')

    return render(request, 'itemServico/excluirItemServico.html', {
        "item": itemExcluir
    })

@login_required
def anexo(request):
        # --- Lista paginada de itens ---
    anexos = Anexos.objects.all().order_by('-id')
    pc = request.GET.get('pc', 1)
    listaAnexos = Paginator(anexos, 3).get_page(pc)

    # --- Cria o formulário (sempre) ---
    formulario = CadastroAnexos_MF(request.POST or None)

    # --- Se o formulário foi enviado e é válido ---
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('anexo')

    # --- Renderiza a página ---
    return render(request, 'anexo/anexo.html', {
        "anexos": listaAnexos,
        "formulario": formulario,
    })
def editarAnexo(request, id):
    anexoEditar = get_object_or_404(Anexos, pk=id)
    formulario = CadastroAnexos_MF(request.POST or None, instance=anexoEditar)

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('anexo') 

    return render(request, 'anexo/editarAnexo.html', {
        'formulario': formulario,
        'anexo': anexoEditar
    })
def excluirAnexo(request, id):
    anexoExcluir = get_object_or_404(Anexos, pk=id)

    if request.method == "POST":
        anexoExcluir.delete()
        return redirect('anexo')  # redireciona para a lista de anexos

    return render(request, 'anexo/excluirAnexo.html', {
        "anexo": anexoExcluir
    })
