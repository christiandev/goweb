# -*- coding: utf-8 -*-
# Autor: christian
from django.shortcuts import render

from .models import CPU, Provedor, Sistema, Armazenamento, Memoria, Produto


def index(request):
    context = {
        'cpus': CPU.objects.all(),
        'provedores': Provedor.objects.all(),
        'sistemas': Sistema.objects.all(),
        'armazenamentos': Armazenamento.objects.all(),
        'memorias': Memoria.objects.all(),
        'produtos': Produto.objects.all(),
    }
    return render(request, 'index.html', context)