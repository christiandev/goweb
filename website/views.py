# -*- coding: utf-8 -*-
# Autor: christian
from django.shortcuts import render
from django.db.models import Q

from .models import CPU, Provedor, Sistema, Armazenamento, Memoria, Produto


def index(request):
    context = {
        'cpus': CPU.objects.all(),
        'provedores': Provedor.objects.all(),
        'sistemas': Sistema.objects.all(),
        'armazenamentos': Armazenamento.objects.all(),
        'memorias': Memoria.objects.all(),
    }

    if request.method == 'GET':
        produtos = Produto.objects.all()
    else:
        data = request.POST
        args = []
        # PROVEDOR
        provedor = data.getlist('provedor')
        if provedor:
            args.append(Q(provedor__in=provedor))
            context.update({'data_provedor': provedor})
        # PREÇO
        preco = data.get('preco')
        if preco:
            args.append(Q(preco__lte=preco))
        # cpu
        cpu = data.get('cpu')
        if cpu:
            args.append(Q(cpu=cpu))
        # MEMÓRIA
        memoria = data.get('memoria')
        if memoria:
            args.append(Q(memoria=memoria))
        # ARMAZENAMENTO
        armazenamento = data.get('armazenamento')
        if armazenamento:
            args.append(Q(armazenamento=armazenamento))
        # SISTEMA
        sistema = data.get('sistema')
        if sistema:
            args.append(Q(sistemas__in=sistema))

        produtos = Produto.objects.filter(*args)

    context.update({'produtos': produtos})
    return render(request, 'index.html', context)
