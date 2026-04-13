import requests
from dataclasses import dataclass


@dataclass
class LoginResult:
    ok: bool
    raw_text: str


def build_query_string(ip: str, mac: str, wlanacname: str, ssid: str, nasip: str, url: str) -> str:
    return (
        f"wlanuserip={ip}&"
        f"wlanacname={wlanacname}&"
        f"ssid={ssid}&"
        f"nasip={nasip}&"
        f"mac={mac}&"
        f"t=wireless-v2-plain&"
        f"url={url}"
    )


def do_login(
    login_api: str,
    username: str,
    password: str,
    query_string: str,
    timeout: int = 10,
) -> LoginResult:
    data = {
        "userId": username,
        "password": password,
        "service": "",
        "queryString": query_string,
        "operatorPwd": "",
        "operatorUserId": "",
        "validcode": "",
        "passwordEncrypt": "false",
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    try:
        resp = requests.post(login_api, data=data, headers=headers, timeout=timeout)
        resp.encoding = resp.apparent_encoding
        text = resp.text
        ok = '"result":"success"' in text
        return LoginResult(ok=ok, raw_text=text)
    except Exception as e:
        return LoginResult(ok=False, raw_text=f"NETWORK_ERROR: {e}")
