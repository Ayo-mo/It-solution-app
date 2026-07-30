# AWS EC2 Server Setup

## Overview

This document describes the process of provisioning and preparing an AWS EC2 server to host the **IT Solution App**. The goal was to create a secure Ubuntu server, configure remote access, install Docker, and prepare the environment for containerized application deployment.

---

# Objectives

* Launch an AWS EC2 instance
* Configure secure remote access using SSH
* Configure networking and security groups
* Install Docker Engine
* Install Docker Compose
* Verify the server is ready for application deployment

---

# Environment

| Component          | Value                         |
| ------------------ | ----------------------------- |
| Cloud Provider     | AWS                           |
| Compute Service    | EC2                           |
| Operating System   | Ubuntu Server 24.04 LTS       |
| Instance Type      | t3.micro (Free Tier Eligible) |
| Authentication     | SSH Key Pair                  |
| Container Platform | Docker                        |
| Orchestration      | Docker Compose                |

---

# Step 1 – Launch EC2 Instance

Created a new EC2 instance with the following configuration:

* Ubuntu Server 24.04 LTS
* 64-bit (x86)
* t3.micro instance type
* 8 GiB storage
* Auto-assign Public IPv4 enabled

---

# Step 2 – Configure Security Group

Configured inbound firewall rules:

| Protocol | Port | Source          |
| -------- | ---- | --------------- |
| SSH      | 22   | My Public IP    |
| HTTP     | 80   | Anywhere (IPv4) |
| HTTPS    | 443  | Anywhere (IPv4) |

These rules allow secure administration while exposing the web application to users.

---

# Step 3 – Create SSH Key Pair

Created an EC2 key pair:

```text
ayo-m-key.pem
```

The private key was stored securely on the local machine and used for SSH authentication.

---

# Step 4 – Connect to the Server

Connected from Git Bash using:

```bash
ssh -i ~/.ssh/ayo-m-key.pem ubuntu@<EC2_PUBLIC_IP>
```

---

# Step 5 – Update Ubuntu

Updated package repositories and upgraded installed packages:

```bash
sudo apt update
sudo apt upgrade -y
```

---

# Step 6 – Install Docker

Installed Docker Engine:

```bash
sudo apt install docker.io -y
```

Enabled and started Docker:

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

Verified installation:

```bash
docker --version
sudo systemctl status docker
```

---

# Step 7 – Install Docker Compose

Installed Docker Compose:

```bash
sudo apt install docker-compose-v2 -y
```

Verified installation:

```bash
docker compose version
```

---

# Verification

The server was successfully prepared for deployment.

Verified:

* Ubuntu updated successfully
* Docker installed and running
* Docker Compose installed
* SSH access working
* HTTP and HTTPS ports configured
* EC2 instance reachable from the Internet

---

# Lessons Learned

* Stopping and starting an EC2 instance changes its public IPv4 address unless an Elastic IP is attached.
* SSH security group rules must be updated if the client's public IP changes.
* Docker should always be verified after installation before deploying applications.
* Keeping SSH keys organized simplifies remote server management.

---

# Next Step

Deploy the containerized Flask application using Docker Compose.
