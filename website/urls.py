# -*- coding: utf-8 -*-
# Autor: christian
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'website.views',
    url(r'^$', 'index', name='index'),
)
