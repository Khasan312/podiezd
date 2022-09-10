from django.shortcuts import render
# from .models import Podiezd

from .payment import make_post_payment

# def post_view(reuqest):
#     if request.method == 'POST':
#         data = make_post_payment(Podiezd.token, 
#                                 Podiezd.account_number,
#                                 Podiezd.refill_date_time,
#                                 Podiezd.amount,
#                                 Podiezd.action
#                                 )
#         data.save()
#     return render (request, 'index.html')

def index(request):
    return render(request, 'index.html' )