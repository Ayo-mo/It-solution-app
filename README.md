# IT Solution App

A production-ready Flask web application built as a hands-on DevOps project. The application demonstrates modern deployment practices using Docker, Docker Compose, Nginx, PostgreSQL, GitHub, and AWS EC2.

---

## Project Overview

This project was built to practice real-world DevOps workflows rather than simply creating a Flask website.

The application runs inside Docker containers, stores data in PostgreSQL, is served through an Nginx reverse proxy, and is deployed to an AWS EC2 Ubuntu server.

---

## Features

* Flask web application
* PostgreSQL database
* Contact form with persistent storage
* Dockerized application
* Docker Compose orchestration
* Gunicorn production server
* Nginx reverse proxy
* Environment variable configuration
* Persistent Docker volumes
* AWS EC2 deployment
* Project documentation
* Changelog

---

## Technology Stack

### Backend

* Python 3.12
* Flask
* SQLAlchemy
* Gunicorn

### Database

* PostgreSQL 16

### Containers

* Docker
* Docker Compose

### Web Server

* Nginx

### Cloud

* AWS EC2 (Ubuntu)

### Version Control

* Git
* GitHub

---

## Project Structure

```text
it-solution-app/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── nginx/
├── static/
├── templates/
├── docs/
│   ├── 01-aws-setup.md
│   ├── 02-ec2-deployment.md
│   ├── 03-ci-cd.md
│   ├── 04-monitoring.md
│   ├── architecture/
│   ├── decisions/
│   ├── engineering-journal/
│   └── releases/
├── CHANGELOG.md
└── README.md
```

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/Ayo-mo/It-solution-app.git
cd It-solution-app
```

Create the environment file:

```bash
cp .env.example .env
```

Start the application:

```bash
docker compose up --build
```

Open:

```
http://localhost
```

---

## Deployment

The production deployment runs on an Ubuntu EC2 instance using Docker Compose.

Current deployment includes:

* Nginx reverse proxy
* Flask application
* PostgreSQL database
* Persistent Docker volume
* Environment variables via `.env`

---

## Documentation

Project documentation is available inside the `docs/` directory.

* AWS Setup
* EC2 Deployment
* CI/CD
* Monitoring
* Architecture
* Engineering Journal
* Release Notes

---

## Changelog

See:

```
CHANGELOG.md
```

for release history.

---

## Current DevOps Features

* Docker containerization
* Docker Compose
* PostgreSQL persistence
* Gunicorn production server
* Nginx reverse proxy
* AWS EC2 deployment
* GitHub version control

---

## Planned Improvements

* GitHub Actions CI/CD
* Docker Hub automated deployments
* HTTPS with Let's Encrypt
* Prometheus monitoring
* Grafana dashboards
* Infrastructure as Code (Terraform)
* Configuration management (Ansible)
* Kubernetes deployment

---

## Author

**Ayodeji (Ayo-mo)**

DevOps & Cloud Engineering Portfolio Project
