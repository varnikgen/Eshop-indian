from django.core.checks.messages import Error
from django.http import HttpResponse
from django.shortcuts import render

from .models.category import Category
from .models.customer import Customer
from .models.product import Product


def index(request):
    products = None
    categories = Category.get_all_categories()

    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_products_by_categoryID(categoryID)
    else:
        products = Product.get_all_products()

    data = {'categories': categories, 'products': products, }
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
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
        
        if not first_name:
            error_message = "Введите Имя!"

        if not last_name:
            error_message = "Введите фамилию!"

        if not phone:
            error_message = 'Заполните поле с номером телефона!'
        if len(phone) < 5:
            error_message = "Номер не может быть меньше 6 символов!"
        elif len(phone) > 12:
            error_message = "Номер слишком длинный!"
        
        # Сохранение
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer = Customer(first_name=first_name, last_name=last_name,
                                phone=phone, email=email, password=password)
            customer.register()
            return render(request, 'index.html')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
