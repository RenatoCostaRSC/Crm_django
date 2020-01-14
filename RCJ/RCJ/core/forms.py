from django import forms
from RCJ.core.models import EnderecoCliente, ContatoCliente, Produto, Client, InfoVenda


class EnderecoClienteForm(forms.ModelForm):
    
    class Meta:
        
        model = EnderecoCliente
        fields = '__all__' 
        
class ContatoClientForm(forms.ModelForm):
    
    class Meta:
        
        model = ContatoCliente
        fields = '__all__' 
        
class ProdutoForm(forms.ModelForm):
    
    class Meta:
        
        model = Produto
        fields= '__all__'

class ClientForm(forms.ModelForm):
    
    class Meta:
        
        model = Client
        exclude = ('endereco', 'contato')
        
class InfoVendaForm(forms.ModelForm):
    
    class Meta:
        
        model = InfoVenda
        exclude = ('cliente','status_auditoria','status_pos_venda','created_date')