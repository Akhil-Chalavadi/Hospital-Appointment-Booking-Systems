# Hospital Appointment Booking System

## Project Overview
The Hospital Appointment Booking System is a web-based application developed to simplify hospital patient management. It allows patients to register, log in, and access their personal dashboard.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- SQLite
- Docker
- Docker Compose
- Selenium (for testing)
- Kubernetes / Minikube (deployment)

## Current Features
1. Patient registration
2. Patient login and authentication
3. Secure password hashing
4. Patient dashboard
5. SQLite database integration
6. Docker containerization

## Project Structure
```text
Hospital_Appointment_System/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── .gitignore
├── static/
└── templates/
```

## How to Run the Project

### Step 1: Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder
```bash
cd Hospital_Appointment_System
```

### Step 3: Build and start using Docker
```bash
docker compose up -d --build
```

### Step 4: Open the application
Open your browser and visit:

http://localhost:5000

## Application Pages
- Home: http://localhost:5000/
- Registration: http://localhost:5000/register
- Login: http://localhost:5000/login
- Dashboard: http://localhost:5000/dashboard

## Stop the Application
```bash
docker compose down
```

## Project Purpose
This project demonstrates web application development, database integration, containerization, and the use of DevOps tools.

## Author
Student Project
