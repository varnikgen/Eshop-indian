from django.contrib.auth.hashers import check_password
from django.views import View
from django.shortcuts import redirect, render, HttpResponseRedirect

from store.models.customer import Customer


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            if check_password(password, customer.password):

                request.session['customer'] = customer.id
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email или пароль не верны!'
        else:
            error_message = 'Email или пароль не верны!'
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
