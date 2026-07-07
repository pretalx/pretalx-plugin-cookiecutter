import shutil
import subprocess
from pathlib import Path

if "github.com" not in "{{ cookiecutter.repo_url }}":
    shutil.rmtree(Path(".github"))

subprocess.run(["uv", "lock"], check=False)
subprocess.run(["just", "fmt"], check=False)
