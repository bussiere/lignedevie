import requests

http_proxy = "http://10.154.61.6:3128"
https_proxy = "http://10.154.61.6:3128"
ftp_proxy = "http://10.154.61.6:3128"

proxies = {"http": http_proxy, "https": https_proxy, "ftp": ftp_proxy}


def send_message_bussiere(
    msg="toto",
    url="https://smsapi.free-mobile.fr/sendmsg",
    user="92342254",
    key="fTJfG5SwBasmG8",
):
    data = {"user": user, "pass": key, "msg": str(msg)}
    r = requests.get(url, params=data, proxies=proxies)
    return r.status_code


msg = """

Bonjour nubothon

"""

try:
    send_message_bussiere(msg)
except:
    import os
    import requests

    os.environ["HTTP_PROXY"] = os.environ["http_proxy"] = "proxy.infra.dgfip:3128"
    os.environ["HTTPS_PROXY"] = os.environ["https_proxy"] = "proxy.infra.dgfip:3128"
    send_message_bussiere(msg)
