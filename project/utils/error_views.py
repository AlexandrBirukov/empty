from django.shortcuts import render


def error_404(request, exception):
    response = render(request, 'errors/404.html', {})
    response.status_code = 404
    return response


def error_403(request, exception=None):
    response = render(request, 'errors/403.html', {})
    response.status_code = 403
    return response


def error_500(request, exception=None):
    response = render(request, 'errors/500.html', {})
    response.status_code = 500
    return response
