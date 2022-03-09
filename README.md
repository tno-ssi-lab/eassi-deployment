# SSI Service Deployment

This repository contains the `docker-compose.yml` files to use locally and in
production.

## Usage

1. Clone this repo.
2. Clone the `eassi-aca-py-server`, `eassi-gateway-backend`, `eassi-gateway-frontend`, and `eassi-irma-server` repos and place them in this repo's directory with names `acapy`, `backend`, `frontend`, and `irma` respectively.
3. Copy `.env.example` to `.env` and update with desired settings (from `ngrok`
   for instance)
4. In production, run
   ```bash
   docker-compose up
   ```
   Locally, run*
   ```
   docker-compose -f docker-compose.dev.yml up
   ```
   *Dev deployment assumes local availability of all the node dependencies for `backend` and `frontend`. These can be installed by
   ```
   docker-compose -f docker-compose.dev.yml run backend npm install
   docker-compose -f docker-compose.dev.yml run frontend yarn install
   ```

Database should be set up automatically.

## ngrok

To be able to use the service locally from a phone that's not on the network, you 
need so set up a proxy service. Ngrok is by far the easiest and free. There is an
example config file included. You still need to register and grab your api key.

After copying the file, you can start ngrok with the following command (skips TCP 
tunnels):

```bash
ngrok start -config=ngrok.yml --all
```

After ngrok has started, you can inspect traffic to your service on http://localhost:4040.

There is a python script included to automatically update your local .env file with
the new proxy settings:

```bash
python3 updatetunnels.py
```
