import subprocess

# installing requirements and making configs
# /usr/local/etc/wg-scripts uses for config files
# scripts copies to /usr/local/bin/

commands = [
    "pip install -r requirements.txt",                                          # python dependencies

    "mkdir /usr/local/etc/wg-scripts",
    "mkdir /usr/local/wireguard",
    "mkdir /usr/local/wireguard/clients",

    # for wg-add
    "cp scripts/wg-add.py /usr/local/bin/wg-add",
    "chmod u+x /usr/local/bin/wg-add",

    # for wg-show
    "cp scripts/wg-show.py /usr/local/bin/wg-show",
    "chmod u+x /usr/local/bin/wg-show",

    # for wg-del
    "cp scripts/wg-del.py /usr/local/bin/wg-del",
    "chmod u+x /usr/local/bin/wg-del",
]

copy_configs = \
    [
        "cp configs/wg_add_config.py /usr/local/etc/wg-scripts/wg_add_config.py",
        "cp configs/wg_show_config.py /usr/local/etc/wg-scripts/wg_show_config.py",
    ]


def execute(commands: list):
    for command in commands:
        print(command)
        try:
            res = subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError as ex:
            res = ex.output.decode()

        if res:
            print(str(res))


if __name__ == "__main__":
    execute(commands)

    while (answer := input('Do you want to update the config files y/n: ')) not in ('y', 'n'):
        print('Incorrect type "y" or "n" (Ctrl+ C to exit)')

    if answer == 'y':
        execute(copy_configs)

