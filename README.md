# Project Name: Advertisment

Welcome to the Advertisment project! This is a Django-based web application that allows users to register and sign in using their email and password. It includes features like custom user models, JWT authentication, and Docker-based deployment.

---
## Technologies Used

- Python 3.12 - Programming language 
- Django 5.1.3 - Backend framework 
- Django REST Framework - API handling 
- PostgreSQL - Database 
- Docker - Containerization 
- JWT - Token-based authentication
---
## Features

- User Authentication:
    - Sign up using email as the username.
    - Sign in with email and password.
    - JWT-based authentication for secure API access.

- Custom User Model:
    - Extended ```AbstractUser``` to use email as the username for user registration.

- Dockerized Application:
    - Both backend and PostgreSQL services run in Docker containers for easy deployment and testing.
---
## Setup
### Requirements

- Python 3.12+ 
- PostgreSQL (for local database use)
- Docker (for containerized development)

### Local Development Setup

**1. Clone the repository:**
```bash
git clone https://github.com/mehrnooshda/advertisment.git
cd advertisment
   ```
    
    

**2. Create a virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
**3. Install dependencies:**
```bash
pip install -r requirements.txt
```
**4. Set up PostgreSQL:**
Ensure you have PostgreSQL running locally, or configure Docker to handle the database (see Docker setup below).

**5. Run migrations:**
```bash
python manage.py migrate
```
**6 .Start the development server:**
```bash
python manage.py runserver
```
  Your Django application should now be running at http://localhost:8000.

### Docker Setup

To simplify local development and deployment, the project comes with Docker.

**1. Build and start the containers:**

```bash 
sudo docker build -t advertisment .
```
This will set up both the Django application and PostgreSQL in containers.

**2. Access the application:**
Visit http://localhost:8000 to interact with the API and the app.

---

## API Endpoints
### Authentication

- POST /signup/
    - Sign up a user with email and password.
    - Body:
```json
    {
      "email": "user@example.com",
      "password": "password123"
    }
```
- POST /signin/

    - Sign in a user with email and password.
    - Body:
```JSON
    {
      "email": "user@example.com",
      "password": "password123"
    }
```

## Testing

To run tests locally:

**1. Set up testing environment:**
    - Ensure PostgreSQL is running or use Docker for PostgreSQL.

**2. Run the tests:**

```PYTHON
python manage.py test
```