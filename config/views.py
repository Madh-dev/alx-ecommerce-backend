from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "status": "running",
        "message": "ALX E-commerce API backend",
        "docs": "/api/docs/",
        "products": "/api/products/",
        "categories": "/api/categories/",
        "auth": {
            "register": "/api/register/",
            "login": "/api/token/",
            "refresh": "/api/token/refresh/",
        }
    })
