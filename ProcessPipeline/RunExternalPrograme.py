import subprocess
from functools import partial
from multiprocessing import Process, Pool
import json
import os
import pathlib

def run_external_prog(cmd_string):
    result = subprocess.run(cmd_string,shell=True,capture_output=True)
    if result.returncode != 0:
        print("Error: In run mfeprimer!")
        print(f"Run command: {cmd_string}")
        print(mfeRunResult.stderr)
        return ""
    else:
        pass
