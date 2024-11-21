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
   - Celery Worker Logs: Check `celery_worker` service in Docker logs.

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
