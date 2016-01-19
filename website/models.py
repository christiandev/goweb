# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail


class CPU(models.Model):
    quantidade = models.PositiveSmallIntegerField(
        help_text="Quantidade de CPU"
    )

    def __unicode__(self):
        return u"{0:d}x".format(self.quantidade)

    class Meta:
        verbose_name_plural = "CPU's"
        unique_together = ['quantidade']
        ordering = ['quantidade']


class Memoria(models.Model):
    quantidade = models.PositiveSmallIntegerField(
        help_text=u"Quantidade de Memória (MB)."
    )

    def __unicode__(self):
        return u"{0:d} MB".format(self.quantidade)

    @property
    def to_gb(self):
        return u"{0:.2f} GB".format(self.quantidade / 1024.)

    class Meta:
        verbose_name = u"Memórias"
        verbose_name_plural = u"Memórias"
        unique_together = ['quantidade']
        ordering = ['quantidade']


class Armazenamento(models.Model):
    quantidade = models.PositiveSmallIntegerField(
        help_text=u"Quantidade de Espaço de Armazenamento (GB)."
    )

    def __unicode__(self):
        return u"{0:d} GB".format(self.quantidade)

    class Meta:
        unique_together = ['quantidade']
        ordering = ['quantidade']


class Sistema(models.Model):
    nome = models.CharField(
        help_text=u"Nome do Sistema Operacional", max_length=150
    )
    arquitetura = models.CharField(
        choices=[("32", "x86"), ("64", "x86_64")], max_length=2
    )

    def __unicode__(self):
        return u"{0} {1}".format(self.nome, self.get_arquitetura_display())

    class Meta:
        unique_together = ['nome', 'arquitetura']
        ordering = unique_together


class Provedor(models.Model):
    nome = models.CharField(
        help_text=u"Nome do Provedor de Serviços", max_length=150
    )
    logo = ImageField(
            upload_to="provedores", help_text=u"Imagem que será exibida na busca"
    )

    def __unicode__(self):
        return u"{0}".format(self.nome)

    def imagem(self):
        if self.logo:
            return u'<img src="%s" />' % get_thumbnail(self.logo, "100", crop='center', quality=95).url
        return ''

    class Meta:
        verbose_name_plural = "Provedores"
        unique_together = ['nome']
        ordering = ['nome']

    imagem.short_description = 'Logo'
    imagem.allow_tags = True


class Produto(models.Model):
    nome = models.CharField(
        help_text=u"Descrição do Produto", max_length=150
    )
    provedor = models.ForeignKey(
        to=Provedor
    )
    preco = models.DecimalField(
        verbose_name=u"Preço", max_digits=5, decimal_places=2
    )
    cpu = models.ForeignKey(
        verbose_name="CPU", to=CPU
    )
    memoria = models.ForeignKey(
        verbose_name=u"Memória", to=Memoria
    )
    armazenamento = models.ForeignKey(
        to=Armazenamento
    )
    sistemas = models.ManyToManyField(
        to=Sistema
    )

    def __unicode__(self):
        return self.nome
