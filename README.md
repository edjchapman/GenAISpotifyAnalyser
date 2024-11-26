# Spotify Analyzer Application

## Overview
A Spotify data analyzer that allows users to authenticate via Spotify, fetch their listening data, and display insights with enhanced visualizations using React.

## Technologies Used
- **Backend**: Django, Django REST Framework, Celery, MySQL, Redis
- **Frontend**: React, Chart.js
- **Task Queue**: Celery, Celery Beat
- **Containerization**: Docker, Docker Compose

## Setup Instructions

### Prerequisites
- Docker and Docker Compose installed
- Spotify Developer Account for API access (Client ID and Secret)

### Setup Steps

1. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd spotify-analyzer
   ```

2. **Environment Configuration**
   Create a `.env` file with the following:
   ```
   SPOTIFY_CLIENT_ID=<your-client-id>
   SPOTIFY_CLIENT_SECRET=<your-client-secret>
   ```

3. **Build and Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Access the Application**
   - Django Backend: [http://localhost:8000](http://localhost:8000)
   - React Frontend: [http://localhost:3000](http://localhost:3000)
   - Celery Worker Logs: Check `celery_worker` service in Docker logs.

5. **Create a Superuser for Django Admin**
   To access the Django admin panel, you need to create a superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
   Follow the prompts to set up your superuser credentials.

   You can access the admin panel at: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Key Features
- Spotify OAuth integration
- Periodic Spotify data fetch using Celery and Celery Beat
- User authentication and social logins using Django-Allauth
- Password reset functionality
- Interactive analysis using React and Chart.js

### Additional Notes
- Update Spotify Developer Dashboard with callback URLs as required.
- Celery Beat is used to automate periodic data fetch tasks.

### Deployment
For production deployment:
- Use Gunicorn for running Django (`gunicorn backend.wsgi:application`).
- Secure database credentials and sensitive settings.

## License
This project is licensed under the MIT License.


## Docker Compose Update

Below is the updated `docker-compose.yml` file to include all required services, 
including backend, database, Redis, Celery workers, and the frontend:

```yaml
services:
  web:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: django_web
    command: >
      sh -c "python manage.py migrate &&
             python manage.py runserver 0.0.0.0:8000"
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    env_file:
      - .env
    depends_on:
      - db
      - redis

  db:
    image: mysql:8.0
    container_name: mysql_db
    environment:
      MYSQL_DATABASE: spotify_analyzer
      MYSQL_USER: user
      MYSQL_PASSWORD: password
      MYSQL_ROOT_PASSWORD: rootpassword
    volumes:
      - db_data:/var/lib/mysql
    ports:
      - "3306:3306"

  redis:
    image: redis:7
    container_name: redis_cache
    ports:
      - "6379:6379"

  celery:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: celery_worker
    command: celery -A backend worker --loglevel=info
    volumes:
      - ./backend:/app
    env_file:
      - .env
    depends_on:
      - redis
      - db

  celery-beat:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: celery_beat
    command: celery -A backend beat --loglevel=info
    volumes:
      - ./backend:/app
    env_file:
      - .env
    depends_on:
      - redis

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    command: npm start
    volumes:
      - ./frontend:/app
    ports:
      - "3000:3000"
    environment:
      - CHOKIDAR_USEPOLLING=true

volumes:
  db_data:
```

### Notes on Docker Compose Update
- **Frontend Service** (`frontend`): This service builds and runs the React frontend.
   - **Build Context**: Points to the `frontend` directory.
   - **Dockerfile**: Uses a Dockerfile specific to the frontend service, which should be located in the `frontend` directory.
   - **Command**: Uses `npm start` to run the development server.
   - **Ports**: Maps port `3000` on the container to port `3000` on your host machine.
   - **Volumes**: Mounts the `frontend` directory to `/app` inside the container to allow hot reloading during development.
   - **Environment**: The environment variable `CHOKIDAR_USEPOLLING=true` is used to ensure that changes are picked up by file watchers inside the container.
