from django.contrib import admin
from .models import Lote

# Register your models here.

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ['area', 'valor', 'localizacao']