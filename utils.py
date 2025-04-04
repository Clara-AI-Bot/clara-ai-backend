import os
import requests

def download_if_missing(url, output_path):
    if not os.path.exists(output_path):
        print(f"Descargando {output_path}...")
        r = requests.get(url)
        with open(output_path, 'wb') as f:
            f.write(r.content)