#!usr/bin/env python3

import requests
import re
from pathlib import Path

TUNNELS = {
    ":3000": "SSI_SERVER_URL",
    ":8080": "BASE_URL",
    ":8088": "IRMASERVER_URL"
}

ENV_FILE = Path("./.env").resolve()

def get_tunnels():
    result = requests.get("http://localhost:4040/api/tunnels").json()

    return { tunnel['config']['addr']: tunnel['public_url'] for tunnel in result['tunnels'] }

def update_env(tunnels):
    if not tunnels:
        return

    with open(ENV_FILE) as f:
        contents = f.read()

    for addr, url in tunnels.items():
        for search, var in TUNNELS.items():
            if search in addr:
                contents = re.sub(f"^{var}\s*=\s*.*$", f"{var}={url}", contents, flags=re.M)

    with open(ENV_FILE, 'w') as f:
        f.write(contents)




if __name__ == "__main__":
    update_env(get_tunnels())
    print("Done")
