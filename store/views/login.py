from django.contrib.auth.hashers import check_password
from django.views import View
from django.shortcuts import redirect, render

from store.models.customer import Customer


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            if check_password(password, customer.password):

                request.session['customer'] = customer.id
                
                return redirect('homepage')
            else:
                error_message = 'Email или пароль не верны!'
        else:
            error_message = 'Email или пароль не верны!'
        return render(request, 'login.html', {'error': error_message})