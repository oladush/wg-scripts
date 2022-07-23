CONFIG_PATH = "/etc/wireguard/wg0.conf"
CLIENT_PATH = "~/wireguard/clients/"
SERVER_PUBLIC_KEY = "YOUR_SERVER_PUBLIC_KEY"
V_NETWORK = "10.0.0.0/24"

template_user_config = """[Interface]
PrivateKey = {pr_key}
Address = {v_addr}
DNS = 8.8.8.8

[Peer]
PublicKey = YOUR_SERVER_PUBLIC_KEY
AllowedIPs = 0.0.0.0/0
Endpoint = SERVER_IP_ADDRESS:SERVER_IP_PORT
"""

template_server_config = """
[Peer]
PublicKey = {pu_key}
AllowedIPs = {v_addr}/32
#Name = {name}
#Description = {description}
"""
