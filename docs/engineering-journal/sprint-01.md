# Sprint 1 – Containerization Foundation

## Sprint Goal

Establish a reproducible development environment using Docker and Docker Compose while adopting a professional Git workflow.

## Objectives

* Containerize the Flask application.
* Build a reusable Docker image.
* Configure Docker Compose for local development.
* Learn the difference between Docker images and containers.
* Understand bind mounts and their use during development.
* Practice feature branching, commits, Pull Requests, and merging.

## Deliverables

* Dockerfile
* .dockerignore
* docker-compose.yml
* Containerized Flask application
* Git feature branch workflow
* Pull Request #1
* Release v0.1.0

## Challenges Encountered

* Flask initially listened only on `127.0.0.1`, making it inaccessible outside the container.
* Learned to expose the application using `host="0.0.0.0"`.
* Understood Docker port publishing and VirtualBox networking.
* Explored bind mounts and their role in speeding up development.

## Hands-on Progress

* Images are immutable templates.
* Containers are running instances of images.
* Docker Compose simplifies multi-container development.
* Small, focused commits make project history easier to understand.
* Pull Requests provide a structured review and merge process.

## Sprint Outcome

The application now runs consistently inside Docker, can be started with Docker Compose, and follows a professional Git workflow with feature branches and Pull Requests.
