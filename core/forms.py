from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="Email", max_length=200)
    assunto = forms.CharField(label="Assunto", max_length=100)
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data["nome"]
        email = self.cleaned_data["email"]
        assunto = self.cleaned_data["assunto"]
        mensagem = self.cleaned_data["mensagem"]

        # Cria o corpo do e-mail
        corpo_email = (
            f"Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}"
        )

        mail = EmailMessage(
            subject=assunto,
            body=corpo_email,
            from_email="leonardogtc@outlook.com",
            to=[email],
            headers={"Reply-To": email},
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco", "estoque", "imagem"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={"class": "form-control"}),
            "estoque": forms.NumberInput(attrs={"class": "form-control"}),
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
