from django.http import JsonResponse

from core.main_proxy_svc import get_proxies_from_freeapiproxies


def get_proxies(request):
    proxy_list = get_proxies_from_freeapiproxies()
    return JsonResponse({"proxy_list": proxy_list})