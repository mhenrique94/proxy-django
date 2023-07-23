import requests
import json

filename = "proxylist.txt"
user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
)

proxy_list = list()


def get_proxies_from_freeapiproxies():
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
