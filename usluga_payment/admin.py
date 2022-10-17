from django.contrib import admin

from usluga_payment.models import Operator, Podiezd, Transaction, Customer

admin.site.register(Podiezd)
admin.site.register(Transaction)
admin.site.register(Operator)
admin.site.register(Customer)

