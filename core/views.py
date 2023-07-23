from http import HTTPStatus
from django.http import JsonResponse

from core.main_proxy_svc import get_proxies_from_freeapiproxies


def get_proxies(request):
    try:
        proxy_list, raw_data = get_proxies_from_freeapiproxies()
    except Exception:
        return JsonResponse(status=HTTPStatus.SERVICE_UNAVAILABLE)
    return JsonResponse({ "proxy_list": proxy_list, "raw_data": raw_data })