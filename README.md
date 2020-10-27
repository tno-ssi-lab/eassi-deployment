# SSI Service Deployment

This repository contains the `docker-compose.yml` files to use locally and in
production.

## Usage

1. Clone this repo.
2. Clone the `backend`, `frontend`, and `irma` repos and place them (with those
   names) in the repo directory.
3. Copy `.env.example` to `.env` and update with desired settings (from `ngrok`
   for instance)
4. In production, run
   ```bash
   docker-compose up
   ```
   Locally, run
   ```
   docker-compose -f docker-compose.dev.yml up
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
