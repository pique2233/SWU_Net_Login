from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm


console = Console()


def banner():
    console.print(Panel.fit("Ruijie 内网登录器", subtitle="default / manual credentials", style="bold cyan"))


def ask_credentials(default_user: str, default_pass: str) -> tuple[str, str]:
    has_default = bool(default_user) and bool(default_pass)

    if has_default:
        use_default = Confirm.ask(
            f"检测到默认账号配置：[{default_user}]，是否使用默认账号登录？",
            default=True,
        )
        if use_default:
            return default_user, default_pass

    user = Prompt.ask("请输入账号", default=(default_user or None))
    # 不回显密码
    pwd = getpass("请输入密码（输入时不显示）：") or default_pass
    return user, pwd


def show_env(ip: str, mac: str):
    console.print(f"[bold]IP[/bold]: {ip}")
    console.print(f"[bold]MAC[/bold]: {mac}")


def show_result(ok: bool, raw_text: str):
    if ok:
        console.print(Panel.fit("✅ 登录成功", style="bold green"))
    else:
        console.print(Panel.fit("❌ 登录失败", style="bold red"))
    console.print(Panel(raw_text[:4000], title="返回内容（截断显示）", style="dim"))
