# EC2 Deployment

## Objective

Deploy the Flask IT Solution application to AWS EC2 using Docker Compose.

## Technologies

- AWS EC2
- Ubuntu
- Docker
- Docker Compose
- Flask
- Gunicorn
- Nginx
- PostgreSQL

## Deployment Steps

- Connected to EC2 via SSH.
- Cloned the GitHub repository.
- Configured the `.env` file.
- Built and started containers with Docker Compose.
- Verified all containers were running.
- Tested the application through the browser.

## Issue Encountered

The Flask container failed to connect to PostgreSQL because the database password contained an `@` character, which caused the manually constructed SQLAlchemy connection string to be parsed incorrectly.

## Resolution

Updated the database password to remove the problematic character, recreated the containers, and verified successful database connectivity.

## Validation

- Website loaded successfully.
- Contact form submitted successfully.
- PostgreSQL stored the submitted records.
- Docker containers remained healthy after deployment.