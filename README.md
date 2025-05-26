# Coffee Shop Management System ☕️

This is a simple Coffee Shop Management application built using Python Flask for the backend and Docker for containerization. It connects to a Microsoft SQL Server database hosted on the developer's machine.

## Features

- Manage Coffee Shop Menu (Add, Delete, Update items)
- Handle customer orders
- Paginated menu display
- SQL Server database integration
- Dockerized for easier deployment

## Project Structure
```
backend/
│
├── app.py                   # Flask main app
├── CoffeeShop_class.py      # Business logic
├── Pagination_class.py      # Pagination helper
├── requirements.txt         # Python dependencies
└── Dockerfile               # Backend Docker image setup

frontend/
│
├── htme/                    # HTML tempaltes
│   ├── home.html
│   ├── layout.html
│   └── …
└── Dockerfile               # Frontend Docker image setup

docker-compose.yaml          # Compose backend service
```
## How to Run

1. Make sure your SQL Server is running and accessible from the Docker container.
2. Update the DB_SERVER, DB_NAME, DB_USER, and DB_PASSWORD environment variables in docker-compose.yaml.
3. Run the app using Docker Compose:
```bash
docker-compose up --build
```
4. Access the app via browser:
 • http://localhost:5000

Notes
 - You must configure your SQL Server to allow remote connections.
 - The backend connects to your host machine using its local IP (e.g., 192.168.x.x).