# -*- coding: utf-8 -*-
# Autor: christian
from django.conf.urls import patterns, url, include

from rest_framework import routers

from .api import ProdutoViewSet


router = routers.SimpleRouter()
router.register(r'produtos', ProdutoViewSet)


urlpatterns = patterns(
    'website.views',
    url(r'^$', 'index', name='index'),
    url(r'^api/v1/', include(router.urls)),
)
