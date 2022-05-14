import subprocess
import json

from cleo.io.io import IO, Verbosity

def existing_gcloud() -> bool:
    cmd = subprocess.run(['gcloud', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return cmd.returncode == 0

def init_glcoud(io: IO):
    cmd = subprocess.run(['gcloud', 'config', 'get-value', 'account'], capture_output=True)
    if b'(unset)' in cmd.stderr:
        io.write_line('It seems <comment>gcloud</comment> cloud is not initialized. Starting <question>`gcloud init`</question>')
        cmd = subprocess.run(['gcloud', 'init'], check=True, stdout=subprocess.PIPE)
        
def load_adc(io: IO):
    cmd = subprocess.run(['gcloud', 'config', 'config-helper', '--format=json'], capture_output=True, universal_newlines=True)
    result = json.loads(cmd.stdout)
    credential = result.get('credential')
    if credential:
        return
    if 'access_token' in credential or 'token_expiry' in credential:
        return
    io.write_line('Missing or expired credentials. Refreshing ADC using <question>`gcloud auth application-default login`</question>')
    cmd = subprocess.run(['gcloud', 'auth', 'application-default', 'login'], capture_output=True)

def authenticate_gcloud(io: IO):
    init_glcoud(io)
    load_adc(io)
