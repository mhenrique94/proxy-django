from ..models import Proxy
from core.api import api


def get_proxies_from_freeapiproxies():
    proxy_list = list()
    try:
        proxies = api.proxies_request()
        raw_data = list()
        for item in proxies:
            raw_data.append(item)
            if len(item["type"]) > 1:
                if "SOCKS5" in item["type"]:
                    item["type"] = "SOCKS5"
                else:
                    item["type"] = "HTTPS"
            else:
                item["type"] = item["type"][0].upper()
            proxy_list.append(
                f'{item["type"].strip()}://{item["ip"].strip()}:{str(item["port"]).strip()}'
            )
        del proxy_list[-1]
    except Exception:
        raise ConnectionError

    return proxy_list, raw_data


def get_proxies_from_db(manual_init=False):
    proxy_list = []
    raw = {}

    proxies = Proxy.objects.all().order_by("-registered_at")[:1000]

    if not proxies or manual_init:
        proxies, raw = get_proxies_from_freeapiproxies()

        for p in raw:
            proxy = Proxy()

            proxy.ip = p["ip"].strip()
            proxy.port = int(str(p["port"]).strip())
            proxy.type = p["type"].strip()
            proxy.country = p["country"].strip()
            proxy.provider = p["provider"].strip()
            proxy.continent = p["continent"].strip()
            proxy.isocode = p["isocode"].strip()
            proxy.region = p["region"].strip()
            proxy.regioncode = p["regioncode"].strip()
            proxy.city = p["city"].strip()
            proxy.latitude = p["latitude"].strip()
            proxy.longitude = p["longitude"].strip()

            proxy.save()

        proxies = Proxy.objects.all().order_by("-registered_at")[:1000]
        for p in proxies:
            serialized_proxy = p.to_dict_json()
            proxy_list.append(serialized_proxy)

        return proxy_list, raw

    for p in proxies:
        serialized_proxy = p.to_dict_json()
        proxy_list.append(serialized_proxy)

    return proxy_list, raw
