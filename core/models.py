from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


# Create your models here.
class Base(models.Model):
    """
    Base model for all models in the app.
    """

    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)
    updated_at = models.DateTimeField("Data de atualização", auto_now=True)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class Produto(Base):
    """
    Model for products.
    """

    nome = models.CharField("Nome", max_length=255)
    preco = models.DecimalField("Preço", max_digits=10, decimal_places=2, default=0.00)
    estoque = models.IntegerField("Estoque", default=0)
    descricao = models.TextField("Descrição")
    imagem = StdImageField(
        "Imagem",
        upload_to="produtos",
        variations={"thumb": {"width": 300, "height": 300, "crop": "smart"}},
    )
    slug = models.SlugField(
        "Slug", max_length=255, unique=True, blank=True, editable=False
    )

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, **kwargs):
    """
    Pre-save signal for Produto model.
    """
    if not instance.slug:
        instance.slug = slugify(instance.nome)
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)
