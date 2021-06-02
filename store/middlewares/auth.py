from django.shortcuts import redirect


def auth_middleware(get_response):

    def middleware(request):
        customer = request.session.get('customer')
        if not customer:
            return redirect('login')

        response = get_response(request)
        return response

    return middleware