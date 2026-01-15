import subprocess


def bad():
    subprocess.run("ls -la", shell=True)  # ❌ sẽ bị Semgrep bắt
