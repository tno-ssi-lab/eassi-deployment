# SSI Service Deployment

This repository contains the `docker-compose.yml` files to use locally and in
production.

## Development Quickstart

1. Clone this repo.
2. Clone the `eassi-aca-py-server`, `eassi-gateway-backend`, `eassi-gateway-frontend`, and `eassi-irma-server` repos and place them in this repo's directory with names `acapy`, `backend`, `frontend`, and `irma` respectively.
3. Copy `.env.example` to `.env` and update with desired settings. The default
   values for all settings should work out of the box, so no configuration
   should be required.
4. Install the dependencies for the backend and frontend modules
   ```
   docker-compose -f docker-compose.dev.yml run backend npm ci
   docker-compose -f docker-compose.dev.yml run frontend yarn install --frozen-lockfile
   ```
5. To locally deploy EASSI, run
   ```
   docker-compose -f docker-compose.dev.yml up
   ```

The database should be set up automatically.

## ngrok

Part of the UX flow is to scan a QR code displayed on the frontend using
a wallet app (of your choice) on your phone. Your phone likely can't communicate
with your locally hosted services by default, which means this won't work.

To be able to use the service locally from a phone that's not on the network,
you need so set up a proxy service. Ngrok is by far the easiest and free. Ngrok
is service to quickly setup a proxy which redirects traffic from a randomly
generated grok subdomain to your services running on localhost. There is an
example config file included.

1. To get started, first [create an account](https://ngrok.com/)
2. The dashboard will show you a command to easily add your authentication token
   to the configuration file. It looks like:
   ```bash
   ngrok config add-authtoken <token>
   ```
3. There is a python script included to automatically update your local .env
   file to work with the proxy.
   ```bash
   python3 updatetunnels.py
   ```
4. Copy the ngrok.yml.example file. ngrok only allows you three tunnels per
   agent on a free account (four are specified in the config file), so you might
   want to remove either the `irma` or `acapy`, depending on which wallet you
   won't be using.
5. After copying the file, you can start ngrok with the following command (skips
   TCP tunnels):
   ```bash
   ngrok start --config=ngrok.yml --all
   ```

After ngrok has started, you can inspect traffic to your service on
`http://localhost:4040`. Here you also find the URLs under which your services
are hosted.
Having started ngrok and updated your `.env` file, you can (re)start
the docker containers.
