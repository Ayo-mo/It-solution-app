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

