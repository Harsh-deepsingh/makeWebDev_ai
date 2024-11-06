# file_utils.py
import json5
import re
from config import FILES

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def load_data_file():
    with open(FILES["data"], 'r') as file:
        data_content = file.read()
        data_content = re.sub(r'^const data = ', '', data_content)
        data_content = re.sub(r';?\s*export\s+default\s+data\s*;', '', data_content)
        data_content = re.sub(r',\s*([\}\]])', r'\1', data_content)
        data = json5.loads(data_content)
        return data

def save_data_file(data):
    with open(FILES["data"], 'w') as file:
        file.write("const data = " + json5.dumps(data, indent=2) + ";\n\nexport default data;")
