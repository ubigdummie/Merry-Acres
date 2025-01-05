import os
import subprocess
import time


def ping(host):
    return (
        subprocess.run(["ping", "-n", "1", host], stdout=subprocess.PIPE).returncode
        == 0
    )


def restart_containers():
    os.system("docker-compose restart")


while True:
    if not ping("8.8.8.8") or not ping("1.1.1.1"):
        print("Internet connection is down. Skipping restart.")
    else:
        print("Internet is up. Checking Docker containers...")
        # Add logic to check container health and restart if necessary
        restart_containers()

    time.sleep(300)  # 5-minute interval
