import subprocess, sys
def self_update():
    subprocess.run(["git","pull"])
    subprocess.run([sys.executable,"core/boot.py"])
if __name__ == "__main__":
    self_update()
