from django.contrib import admin

from usluga_payment.models import BaipInfo, Podiezd, Transaction

admin.site.register(Podiezd)
admin.site.register(Transaction)
admin.site.register(BaipInfo)
