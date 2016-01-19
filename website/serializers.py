# -*- coding: utf-8 -*-
# Autor: christian
from rest_framework import serializers

from .models import Memoria, Produto, Provedor, CPU, Armazenamento, Sistema


class ProvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provedor
        fields = ('id', 'nome', 'imagem')


class MemoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memoria
        fields = ('id', 'quantidade')


class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = ('id', 'quantidade')


class ArmazenamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armazenamento
        fields = ('id', 'quantidade')


class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = ('id', 'nome', 'arquitetura')


class ProdutoSerializer(serializers.ModelSerializer):
    memoria = MemoriaSerializer(required=False)
    provedor = ProvedorSerializer(required=False)
    cpu = CPUSerializer(required=False)

    class Meta:
        model = Produto
        fields = ('id', 'nome', 'provedor', 'preco', 'cpu', 'armazenamento', 'sistemas', 'memoria')
