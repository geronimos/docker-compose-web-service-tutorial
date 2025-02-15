# Docker Compose for Web Services - A Simple Example

A multi-service setup demonstration using Docker Compose, featuring three services:

1. **Books Service** (Python + Flask)
2. **Fruits Service** (Python + Flask)
3. **Website** (PHP + Apache)

## Technologies Used

- **Languages**: Python, PHP
- **Tools**: Docker, Docker Compose, Flask
- **Web Server**: Apache

## Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/docker-compose-web-service-tutorial.git
   cd docker-compose-web-service-tutorial
   ```

2. **Build and start services**

   ```bash
   docker-compose up --build
   ```

3. **Access the services**

   - Books Service: http://localhost:5001
   - Fruits Service: http://localhost:5002
   - Website: http://localhost:5003

4. **Stop the services**

   ```bash
   docker-compose down
   ```

## Project Structure

Each service has its own `Dockerfile` and source code. The website demonstrates integration with the Python services through a simple PHP interface.

## What This Example Demonstrates

- Setting up multiple services with Docker Compose
- Service communication in a containerized environment
- Integration between PHP and Python services
- Basic Docker Compose configuration and usage

## References

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PHP Apache Docker Image](https://hub.docker.com/_/php)
- [Docker Compose Tutorial](https://www.youtube.com/watch?v=Qw9zlE3t8Ko)
