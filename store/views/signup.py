from django.contrib.auth.hashers import make_password
from django.views import View
from django.shortcuts import redirect, render

from store.models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Проверка
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        error_message = None

        customer = Customer(first_name=first_name, last_name=last_name,
                            phone=phone, email=email, password=password)

        error_message = self.validateCustomer(customer)

        # Сохранение
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "Введите Имя!"

        if not customer.last_name:
            error_message = "Введите фамилию!"

        if not customer.phone:
            error_message = 'Заполните поле с номером телефона!'
        if len(customer.phone) < 5:
            error_message = "Номер не может быть меньше 6 символов!"
        elif len(customer.phone) > 12:
            error_message = "Номер слишком длинный!"

        if customer.isExists():
            error_message = "Данный email-адрес уже используется!"

        return error_message
