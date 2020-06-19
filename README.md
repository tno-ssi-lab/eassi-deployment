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
   docker-compose up -f docker-compose.dev.yml
   ```

Database should be set up automatically.