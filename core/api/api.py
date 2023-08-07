import requests
import json

from proxydjango import settings

user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
)


def proxies_request():
    if settings.DEBUG:
        f = open("core/api/data.json")
        data = json.load(f)
        return data["proxy_list"]
    else:
        proxy_site_url = "https://freeapiproxies.azurewebsites.net/proxyapi?count=1000"
        res = requests.get(proxy_site_url, headers={"User-Agent": user_agent})
        return json.loads(res.text)
