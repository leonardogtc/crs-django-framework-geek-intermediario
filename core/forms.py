from django import forms
from django.core.mail.message import EmailMessage


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
