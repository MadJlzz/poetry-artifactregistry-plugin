import subprocess

def existing_gcloud() -> bool:
    cmd = subprocess.run(['gcloud','--version'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return cmd.returncode == 0
