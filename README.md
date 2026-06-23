# AI DevOps Assignment – Webvory

## Project Overview

This project demonstrates production deployment of a FastAPI backend using Docker and VPS infrastructure.

The stack includes:

* FastAPI
* PostgreSQL
* Redis
* NGINX Reverse Proxy
* Docker Compose
* GitHub Actions CI/CD
* Azure VPS

---

## Architecture

User → NGINX → FastAPI → PostgreSQL
↘ Redis Cache

---

## Services

### FastAPI

Handles API requests and health checks.

### PostgreSQL

Stores application data.

### Redis

Used for caching and background job support.

### NGINX

Acts as reverse proxy.

---

## Deployment Setup

### Clone repository

```bash
git clone <repo_url>
cd ai-devops-assignment
```

### Run application

```bash
docker-compose up -d --build
```

---

## Health Check

Endpoint:

```bash
/health
```

Response:

```json
{
  "status": "healthy"
}
```

---

## CI/CD Pipeline

Implemented using GitHub Actions.

Workflow:

1. Push code to main branch
2. GitHub Actions triggers deployment
3. Connects to Azure VPS over SSH
4. Pulls latest code
5. Rebuilds Docker containers
6. Restarts application

---

## Security Measures

* UFW firewall enabled
* SSH key-based authentication
* Environment variables separated via `.env`
* Reverse proxy isolation via NGINX

---

## SSL Setup

If domain is available:

* Use Let's Encrypt
* Configure via Certbot

Current deployment uses HTTP because domain is not configured.

---

## Logging Strategy

* Docker logs
* NGINX logs
* Application logs

Commands:

```bash
docker logs fastapi_app
docker logs nginx_proxy
```

---

## Backup Strategy

PostgreSQL data persisted using Docker volumes.

Backup example:

```bash
docker exec postgres_db pg_dump -U admin appdb > backup.sql
```

---

## Monitoring

Basic health checks enabled.

Future improvements:

* Prometheus
* Grafana
* Fail2ban
* Cloudflare

---

## Live Deployment

Application:
http://20.219.65.113:8080

Health:
http://20.219.65.113:8080/health
