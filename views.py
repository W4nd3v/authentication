from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib import messages, auth
from django.contrib.auth.models import User

''' PÓS CURSO 
    Área do usuário:
        foto,
        mudar nome,
        mudar senha
    Login:
        recuperar senha,
        '''

def login(request):
    variavel_form = LoginForms()
    # valida e guarda o formulário na variável no form
    if request.method == 'POST': 
        form = LoginForms(request.POST)
        #valida formulário
        if form.is_valid(): 
            # verficando se o usuário do form existe no banco
            nome = form['nome_login'].value()
            usuario = auth.authenticate( 
                request,
                username = nome,
                password = form['senha'].value()
            )
            # Logando
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Olá, {nome}!')
                return redirect('index')
            else:
                messages.error(request, f'Usuário e senha inválidos.')
                return redirect('login')
    return render(request, 'usuarios/login.html', {'form': variavel_form})

def cadastro(request):
    # Melhorar sistema de login colocando tudo minúsculo e espaço
    # Dividir o campo nome de cadastro, no forms, em 'Nome completo' e login
    # Verificação automática no próprio campo
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        # verific. validade do formulário
        if form.is_valid():   
            # verfic. usuario de mesmo nome
            if User.objects.filter(username=form['nome_cadastro'].value()).exists():
                messages.error(request, 'Já existe um usuário cadastrado com este nome')
                return redirect('cadastro')
            # Cadastrando user in banco
            usuario = User.objects.create_user(
                username = form['nome_cadastro'].value(),
                email = form['email'].value(),
                password = form['senha'].value() 
            )
            usuario.save()
            messages.success(request, 'Usuário cadastrado!')
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form':form})

def logout(request):
    auth.logout(request)
    messages.warning(request, 'Você saiu!')
    return redirect('login')