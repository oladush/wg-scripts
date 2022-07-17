import subprocess

# make directory in /usr/local/etc for configs

commands = [
    "pip install -r requirements.txt",
    "mkdir /usr/local/etc/wg-scripts",
    "cp configs/wg_add_config.py /usr/local/etc/wg-scripts/wg_add_config.py",
    "cp scripts/wg-add.py /usr/local/bin/wg-add",
    "chmod u+x /usr/local/bin/wg-add",
]

for command in commands:
    print(command)
    try:
        res = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as ex:
        res = ex.output.decode()

    if res:
        print(str(res))