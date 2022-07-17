CONFIG_PATH = "/etc/wireguard/wg0.conf"
CLIENT_PATH = "/home/old/wireguard/clients/"
SERVER_PUBLIC_KEY = "UUJ/uhzzf5QcSRjA5Qz/CpCFeXjUFLyx6g3U9oA3/1w="
V_NETWORK = "10.0.0.0/24"

template_user_config = """[Interface]
PrivateKey = {pr_key}
Address = {v_addr}
DNS = 8.8.8.8

[Peer]
PublicKey = UUJ/uhzzf5QcSRjA5Qz/CpCFeXjUFLyx6g3U9oA3/1w=
AllowedIPs = 0.0.0.0/0
Endpoint = 185.18.54.215:51820
"""

template_server_config = """
[Peer]
PublicKey = {pu_key}
AllowedIPs = {v_addr}/32
#{description}
"""
