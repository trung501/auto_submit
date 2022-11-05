import subprocess
from time import sleep

while True:
    p = subprocess.Popen("python3 pwn2.py", shell=True)
    sleep(60)
