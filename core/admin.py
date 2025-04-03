from django.contrib import admin
from .models import Produto


# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "slug",
        "preco",
        "estoque",
        "descricao",
        "created_at",
        "updated_at",
        "ativo",
    )
    search_fields = ("nome",)
    list_filter = ("nome",)
    ordering = ("-id",)
    list_per_page = 10
