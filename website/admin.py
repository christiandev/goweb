# -*- coding: utf-8 -*-
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import CPU, Provedor, Sistema, Armazenamento, Memoria, Produto


@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    pass


@admin.register(Memoria)
class MemoriaAdmin(admin.ModelAdmin):
    list_display = ['quantidade', 'to_gb']


@admin.register(Armazenamento)
class ArmazenamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_filter = ['arquitetura']


@admin.register(Provedor)
class ProvedorAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['nome', 'imagem']
    search_fields = ['nome']


@admin.register(Produto)
class ProvedorAdmin(admin.ModelAdmin):
    filter_horizontal = ['sistemas']
    list_display = ['nome', 'provedor', 'preco', 'cpu', 'memoria', 'armazenamento']
    list_filter = ['provedor', 'cpu', 'memoria', 'armazenamento', 'sistemas']
    search_fields = ['nome', 'preco']
