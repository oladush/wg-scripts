import subprocess

# make directory in /usr/local/etc for configs

commands = [
    "pip install -r requirements.txt",
    "mkdir /usr/local/etc/wg-scripts",
    "cp configs/wg_add_config.py /usr/local/etc/wg-scripts/wg_add_config.py",
    "cp scripts/wg-add.py /usr/local/bin/wg-add",
    "chmod u+x /usr/local/bin/wg-add",
]
subprocess.check_output(f"pip install -r requirements.txt", shell=True)
subprocess.check_output(f"mkdir /usr/local/etc/wg-scripts", shell=True)
subprocess.check_output(f"cp configs/wg_add_config.py /usr/local/etc/wg-scripts/wg_add_config.py", shell=True)
subprocess.check_output(f"cp scripts/wg-add.py /usr/local/bin/wg-add", shell=True)
subprocess.check_output(f"chmod u+x /usr/local/bin/wg-add", shell=True)


for command in commands:
    print(command)
    try:
        res = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as ex:
        res = ex.output.decode()
    print(res)