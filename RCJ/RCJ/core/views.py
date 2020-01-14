from RCJ.core.forms import EnderecoClienteForm, ContatoClientForm, ProdutoForm, ClientForm, InfoVendaForm
from django.shortcuts import render, redirect


# Create your views here.

def create_produto(request):
    template_name = 'core/create_produto.html'
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('#')
    else:
        form = ProdutoForm()
    context = {
        'form':form
    }
    return render(request, template_name, context)
            

def implanta_ficha_cliente(request):
    template_name = 'core/implanta_ficha.html'
    if request.method == 'POST':
        form1 = ClientForm(request.POST)
        form2 = EnderecoClienteForm(request.POST)
        form3 = ContatoClientForm(request.POST)
        form4 = InfoVendaForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            endereco = form2.save()
            contato = form3.save()
            cliente = form1.save(commit = False)
            cliente.endereco = endereco
            cliente.contato = contato
            cliente.save()
            venda = form4.save(commit = False)
            venda.cliente = cliente
            venda.save()
            return redirect('#')
    else:
        form1 = ClientForm()
        form2 = EnderecoClienteForm()
        form3 = ContatoClientForm()
        form4 = InfoVendaForm()
    context = {
        'form1':form1,
        'form2':form2,
        'form3':form3,
        'form4':form4,
    }
    return render(request, template_name, context)        
            
        
