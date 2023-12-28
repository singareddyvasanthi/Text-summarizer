import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

poject_name = "textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{poject_name}/__init__.py",
    f"src/{poject_name}/components/__init__.py",
    f"src/{poject_name}/utils/__init__.py",
    f"src/{poject_name}/utils/common.py"
    f"src/{poject_name}/logging/__init__.py",
    f"src/{poject_name}/config/__init__.py",
    f"src/{poject_name}/config/configuration.py",
    f"src/{poject_name}/pipeline/__init__.py",
    f"src/{poject_name}/entity/__init__.py",
    f"src/{poject_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setip.py",
    "research/trials.ipynb.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"creating empty file: {filepath}")
        
    else:
        logging.info(f"{filename} already exists")
print("pythonn")