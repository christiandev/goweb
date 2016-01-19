import os
import django
from django.test.client import RequestFactory

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ppc.settings")
django.setup()

from website.models import Produto
from website.serializers import ProdutoSerializer




produto = Produto.objects.all().first()
context = dict(request=RequestFactory().get('/'))
serialize = ProdutoSerializer(produto, context=context)

print(serialize.data)
