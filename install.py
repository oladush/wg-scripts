import subprocess

# installing requirements and making configs
# /usr/local/etc/wg-scripts uses for config files
# scripts copies to /usr/local/bin/

commands = [
    "pip install -r requirements.txt",                                          # python dependencies

    "mkdir /usr/local/etc/wg-scripts",
    "mkdir /usr/local/wireguard/clients",

    "cp configs/wg_add_config.py /usr/local/etc/wg-scripts/wg_add_config.py",   # for wg-add
    "cp scripts/wg-add.py /usr/local/bin/wg-add",
    "chmod u+x /usr/local/bin/wg-add",

    "cp configs/wg_show_config.py /usr/local/etc/wg-scripts/wg_show_config.py",  # for wg-show
    "cp scripts/wg-show.py /usr/local/bin/wg-show",
    "chmod u+x /usr/local/bin/wg-show",
]

for command in commands:
    print(command)
    try:
        res = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as ex:
        res = ex.output.decode()

    if res:
        print(str(res))