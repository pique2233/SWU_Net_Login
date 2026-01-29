import socket
import uuid


def get_local_ip(gateway_ip: str) -> str:
    """获取本机内网出口 IP（通过 UDP connect 触发系统选路，不真正发包）"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect((gateway_ip, 80))
        ip = s.getsockname()[0]
        return ip
    finally:
        s.close()


def get_mac_address() -> str:
    """获取本机 MAC（12 位十六进制，不含冒号）"""
    mac_hex = hex(uuid.getnode())[2:].zfill(12)
    return mac_hex[-12:]
