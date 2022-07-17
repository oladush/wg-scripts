import subprocess

# make directory in /usr/local/etc for configs

subprocess.check_output(f"pip install -r requirements.txt", shell=True)
subprocess.check_output(f"mkdir /usr/local/etc/wg-scripts", shell=True)
subprocess.check_output(f"cp configs/wg_add_config.py /usr/local/etc/wg-scripts/wg_add_config.py", shell=True)
subprocess.check_output(f"cp scripts/wg-add.py /usr/local/bin/wg-add", shell=True)
subprocess.check_output(f"chmod u+x /usr/local/bin/wg-add", shell=True)
