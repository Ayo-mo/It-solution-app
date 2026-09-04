# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** and this project follows **Semantic Versioning**.

---

## [0.2.0] - 2026-07-31

### Added

* Dockerized the Flask application.
* Added PostgreSQL database support using Flask-SQLAlchemy.
* Added persistent database storage using Docker volumes.
* Added Nginx reverse proxy.
* Added project documentation under the `docs/` directory.
* Added EC2 deployment documentation.
* Added AWS setup documentation.

### Changed

* Configured the application to use environment variables.
* Improved Docker Compose configuration.
* Configured Gunicorn as the production WSGI server.
* Improved project folder organization.

### Fixed

* Fixed PostgreSQL hostname configuration.
* Fixed Docker networking between Flask and PostgreSQL containers.
* Fixed database authentication issues caused by special characters in environment variables.
* Verified data persistence after container recreation.
* Cleaned deployment configuration.


### CI/CD

* Added GitHub Actions CI/CD pipeline for the Flask application.
* Added automated Python dependency installation and syntax validation.
* Added automated Docker image builds.
* Added automated Docker image publishing to Docker Hub.
* Added automated deployment to AWS EC2 through SSH.
* Added separate `build-and-test`, `docker-build-and-push`, and `deploy-to-ec2` pipeline stages.
* Added Docker image tagging with both `latest` and Git commit SHA.
* Verified successful end-to-end deployment from GitHub Actions to the EC2 production server.
* Verified the deployed Flask application through Nginx on port 80.
* Verified that the production web container runs with Gunicorn.
* Verified PostgreSQL and persistent Docker volume operation.
* Confirmed the deployed Docker image SHA matched the image produced by the CI/CD pipeline.
* Confirmed the live application was accessible and functioning through the production server.


---

## [0.1.0] - 2026-07-26

### Added

* Initial Flask application.
* Static pages:

  * Home
  * About
  * Services
  * Contact
* Docker support.
* Initial GitHub repository.
* Initial project documentation.

