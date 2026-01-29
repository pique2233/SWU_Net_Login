import socket
import uuid


def get_local_ip(gateway_ip: str) -> str:
    """获取本机内网出口 IP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect((gateway_ip, 80))
        ip = s.getsockname()[0]
        return ip
    finally:
        s.close()


def get_mac_address() -> str:
    """获取本机 MAC"""
    mac_hex = hex(uuid.getnode())[2:].zfill(12)
    return mac_hex[-12:]
