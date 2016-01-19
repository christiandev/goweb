# -*- coding: utf-8 -*-
# Autor: christian

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response


from .serializers import ProdutoSerializer
from .models import Produto


class ProdutoViewSet(viewsets.ModelViewSet):
    model = Produto
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Produto.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Produto não pode ser criado com os dados recebidos.'
        }, status=status.HTTP_400_BAD_REQUEST)