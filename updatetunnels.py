#!usr/bin/env python3

import requests
import re
import os
import subprocess
from pathlib import Path

TUNNELS = {
    ":3000": "SSI_SERVER_URL",
    ":8080": "BASE_URL",
    ":8088": "IRMASERVER_URL",
    ":9000": "ACAPY_ENDPOINT"
}

ENV_FILE = Path("./.env").resolve()

def get_tunnels():
    result = requests.get("http://localhost:4040/api/tunnels").json()
    return { tunnel['config']['addr']: tunnel['public_url'] for tunnel in result['tunnels'] }

def get_tunnels_gitpod():
    return {
        tunnel: subprocess.run(f"gp url {tunnel[1:]}", shell=True, check=True, capture_output=True, text=True).stdout.strip() for tunnel in TUNNELS.keys()
    }

def update_env(tunnels):
    updated = 0

    if not tunnels:
        return updated

    with open(ENV_FILE) as f:
        contents = f.read()

    for addr, url in tunnels.items():
        for search, var in TUNNELS.items():
            if search in addr:
                updated += 1
                contents = re.sub(f"^{var}\s*=\s*.*$", f"{var}={url}", contents, flags=re.M)

    with open(ENV_FILE, 'w') as f:
        f.write(contents)

    return updated


if __name__ == "__main__":
    tunnels = get_tunnels_gitpod() if "GITPOD_HOST" in os.environ else get_tunnels()
    updated = update_env(tunnels)
    print(f"Done. Updated {updated} tunnels.")
