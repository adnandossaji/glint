import markdown
import yaml
import os
import subprocess
import json
import re
from datetime import datetime

def generate():
    config = load_config()
    content_dir = config['content_dir']
    os.makedirs('dist', exist_ok=True)

    for file_name in os.listdir(content_dir):
        if file_name.endswith('.yaml'):
            yaml_file_path = os.path.join(content_dir, file_name)
            subprocess.run(['node', 'render.js', yaml_file_path])
            print(f"Generated HTML for: {file_name}")

def load_config():
    with open("glint.yaml", "r") as f:
        return yaml.safe_load(f)
