import time
from rich.console import Console

from .config import load_config
from .net import get_local_ip, get_mac_address
from .client import build_query_string, do_login
from .ui import banner, ask_credentials, show_env, show_result

console = Console()


def run():
    cfg = load_config()

    banner()

    if cfg.sleep_seconds > 0:
        console.print(f"[dim]启动前等待 {cfg.sleep_seconds}s...[/dim]")
        time.sleep(cfg.sleep_seconds)

    ip = get_local_ip(cfg.gateway_ip)
    mac = get_mac_address()

    show_env(ip, mac)

    username, password = ask_credentials(cfg.username, cfg.password)
    if not username or not password:
        console.print("[bold red]账号/密码为空，已退出。[/bold red]")
        return

    qs = build_query_string(
        ip=ip,
        mac=mac,
        wlanacname=cfg.wlanacname,
        ssid=cfg.ssid,
        nasip=cfg.nasip,
        url=cfg.url,
    )

    result = do_login(
        login_api=cfg.login_api,
        username=username,
        password=password,
        query_string=qs,
    )

    show_result(result.ok, result.raw_text)


if __name__ == "__main__":
    run()
