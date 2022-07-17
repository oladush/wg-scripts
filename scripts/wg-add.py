import re
import ipaddress
import subprocess
from typing import Optional

config_path = "/usr/local/etc/wg-scripts/wg-add-config.py"

def make_configs(v_ip: str, user: str) -> (str, str):
    print("Starting key generation...")

    pr_key = subprocess.check_output("wg genkey", shell=True).decode()[:-1]
    pu_key = subprocess.check_output(f"echo {pr_key} | wg pubkey", shell=True).decode()[:-1]

    print("Private key: %s" % pr_key)
    print("Public key: %s" % pu_key)

    client_config = template_user_config.format(pr_key=pr_key, v_addr=v_ip)
    server_config = template_server_config.format(pu_key=pu_key, v_addr=v_ip, description=user)

    return client_config, server_config


def search_available_ip() -> Optional[str]:
    with open(CONFIG_PATH, "r") as rf:
        config = rf.read()

    for ip in ipaddress.IPv4Network(V_NETWORK):
        if not re.search(str(ip), config):
            return str(ip)


def write_server_config(conf: str):
    with open(CONFIG_PATH, "a") as wf:
        wf.write(conf)


def write_client_config(conf:str, user:str):
    path = CLIENT_PATH + user + '/'
    print(f"Creating directory: { path }")
    subprocess.check_output(f"mkdir { path }", shell=True)

    with open(f"{ path + user }.conf", "w") as wf:
        wf.write(conf)

    qr = subprocess.check_output(f"qrencode -t ansiutf8 < { path + user }.conf", shell=True)
    subprocess.check_output(f"qrencode -t png -o { path }qr.png -r { path + user }.conf", shell=True)
    subprocess.check_output(f"qrencode -t ansiutf8 < { path + user }.conf > { path }qr.txt", shell=True)
    print(qr.decode())


if __name__ == '__main__':
    print("Searching available ip..")
    ip = search_available_ip()

    if ip:
        print("Success, ip is %s" % ip)
    else:
        print("Available is not founded")
        exit(1)

    username = input("Type name of new user\n# ")

    if not username:
        print("Set name of user")
        exit(1)

    print("Making configs..")
    client, server = make_configs(ip, username)

    write_server_config(server)
    write_client_config(client, username)

    print("You can type it:")
    print("cat /etc/wireguard/wg0.conf")
    print("wg-quick down wg0; wg-quick up wg0")
    print(f"cd {CLIENT_PATH}{username}")