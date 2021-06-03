from django.shortcuts import redirect


def auth_middleware(get_response):

    def middleware(request):
        return_url = request.META['PATH_INFO']
        customer = request.session.get('customer')
        if not customer:
            return redirect(f'login?return_url={return_url}')

        response = get_response(request)
        return response

    return middleware