import requests
import json
from .models import Proxy

filename = "proxylist.txt"
user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
)


def get_proxies_from_freeapiproxies():
    proxy_list = list()
    try:
        proxy_site_url = "https://freeapiproxies.azurewebsites.net/proxyapi?count=1000"
        res = requests.get(proxy_site_url, headers={"User-Agent": user_agent})
        proxies = json.loads(res.text)
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
                f'{item["type"].strip()}://{item["ip"].strip()}:{item["port"].strip()}'
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
            proxy.port = int(p["port"].strip())
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
            proxy.portPreferred = int(p["portPreferred"].strip())

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
