from django import forms

'''Fazer validação:
    - maiúsculas; 
    - minúsculas;
    - número;
    - caractere especial
    - quantidade mínima de caracteres'''
    
class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'Nome de Login', #vai aparecer como descrição do field
        required = True, #obrigatóriedade do field (campo)
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Yan Lucas'
            }
        )
    )
    senha = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 100,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }            
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = 'Nome Completo', 
        required = True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Alice Campos Belo'
            }
        )            
    )
    email = forms.EmailField(
        label = 'Email', 
        required = True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.: alice@campos.com.br'
            }            
        )
    )
    senha = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 100,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }            
        )
    )
    conf_senha = forms.CharField(
        label = 'Confirme sua Senha',
        required = True,
        max_length = 100,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirme sua senha'
            }            
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é permitido espaço nesse campo.')
            else:
                return nome

    def clean_conf_senha(self):
        senha = self.cleaned_data.get('senha')
        conf_senha = self.cleaned_data.get('conf_senha')
        if senha != conf_senha:
            raise forms.ValidationError('As senhas não coincidem!')
        else:
            return conf_senha
