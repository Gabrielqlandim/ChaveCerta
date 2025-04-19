from django.contrib import admin
from .models import Imovel, ContratoLocacao, Pagamento, Avaliacao

# Register your models here.

admin.site.register(Imovel)
admin.site.register(ContratoLocacao)
admin.site.register(Pagamento)
admin.site.register(Avaliacao)