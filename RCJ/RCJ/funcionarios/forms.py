from .models import Funcionario, Endereco, Rg, Cpf, TituloDeEleitor
from django import forms


class FuncionarioForm(forms.ModelForm):
    
    class Meta:
        
        model = Funcionario
        exclude = ('rg','cpf','voter_title','adress','slug')

class EnderecoForm(forms.ModelForm):
    
    class Meta:
        
        model = Endereco
        fields = '__all__'
        
class RgForm(forms.ModelForm):
    
    class Meta:
        
        model = Rg
        fields = '__all__'
                
class CpfForm(forms.ModelForm):
    
    class Meta:
        
        model = Cpf
        fields = '__all__'
        
class TituloDeEleitorForm(forms.ModelForm):
    
    class Meta:
        
        model = TituloDeEleitor
        fields = '__all__'
        