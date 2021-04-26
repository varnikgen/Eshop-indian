from django.contrib.auth.hashers import make_password, check_password
from django.core.checks.messages import Error
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models.category import Category
from .models.customer import Customer
from .models.product import Product


print(make_password('123'))


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


def validateCustomer(customer):
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

def registerUser(request):
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

    error_message = validateCustomer(customer)

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

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            if check_password(password, customer.password):
                return redirect('homepage')
            else:
                error_message = 'Email или пароль не верны!'
        else:
            error_message = 'Email или пароль не верны!'
        return render(request, 'login.html', {'error': error_message})
