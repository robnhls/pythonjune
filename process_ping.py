import shlex
import subprocess

cmd = shlex.split("ping -n 1 10.24.100.139")

try:
    response = subprocess.check_output(cmd)
    print(response)
    print("the machine is 'alive'")
except subprocess.CalledProcessError:
    print("looks like it is down")
