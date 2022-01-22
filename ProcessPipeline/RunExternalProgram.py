import subprocess
import os
import pathlib

def run_external_prog(call_func, cmd_string, **kargs):
    result = subprocess.run(cmd_string,shell=True,capture_output=True)
    if result.returncode != 0:
        print("Error: In run mfeprimer!")
        print(f"Run command: {cmd_string}")
        print(result.stderr.decode())
        return ""
    else:
        if call_func:
            return call_func(result.stdout.decode(),**kargs)
        else:
            return result.stdout.decode()
