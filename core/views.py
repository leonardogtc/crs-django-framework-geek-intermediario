from django.shortcuts import render
from django.contrib import messages

from core.forms import ContatoForm


def index(request):
    return render(request, "index.html")


def contato(request):
    # Instancia o formulário informando que pode estar vazio ou ter recebido POST
    form = ContatoForm(request.POST or None)

    # Verifica se o formulário foi enviado e é válido
    if request.method == "POST" and form.is_valid():
        # Armazenar em variáveis
        nome = form.cleaned_data["nome"]
        email = form.cleaned_data["email"]
        assunto = form.cleaned_data["assunto"]
        mensagem = form.cleaned_data["mensagem"]

        # Aqui você pode processar os dados do formulário
        # Por exemplo, enviar um e-mail ou salvar em um banco de dados
        print("Formulário enviado com sucesso!")
        print("Nome:", {nome})
        print("Email:", {email})
        print("Assunto:", {assunto})
        print("Mensagem:", {mensagem})

        messages.success(request, "Mensagem enviada com sucesso!")
        form = ContatoForm()  # Limpa o formulário após o envio

    else:
        messages.error(request, "Erro ao enviar a mensagem. Tente novamente.")

    context = {
        "form": form,
    }

    return render(request, "contato.html", context)


def produto(request):
    return render(request, "produto.html")
