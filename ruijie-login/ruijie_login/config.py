from dataclasses import dataclass
import os
from dotenv import load_dotenv


@dataclass
class RuijieConfig:
    username: str
    password: str
    login_api: str
    gateway_ip: str
    wlanacname: str
    ssid: str
    nasip: str
    url: str
    sleep_seconds: int


def load_config() -> RuijieConfig:
    load_dotenv()  # 自动读取 .env（如果存在）

    def getenv(key: str, default: str = "") -> str:
        return os.getenv(key, default).strip()

    sleep_s = getenv("RUIJIE_SLEEP_SECONDS", "10")
    try:
        sleep_seconds = int(sleep_s)
    except ValueError:
        sleep_seconds = 10

    return RuijieConfig(
        username=getenv("RUIJIE_USERNAME", ""),
        password=getenv("RUIJIE_PASSWORD", ""),
        login_api=getenv("RUIJIE_LOGIN_API", "http://222.198.127.170/eportal/InterFace.do?method=login"),
        gateway_ip=getenv("RUIJIE_GATEWAY_IP", "222.198.127.170"),
        wlanacname=getenv("RUIJIE_WLANACNAME", "NAS"),
        ssid=getenv("RUIJIE_SSID", "Ruijie"),
        nasip=getenv("RUIJIE_NASIP", "172.28.255.4"),
        url=getenv("RUIJIE_URL", "http://123.123.123.123/"),
        sleep_seconds=sleep_seconds,
    )
