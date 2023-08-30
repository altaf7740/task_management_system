# Task Management System API

## Description

The Task Management System API is a RESTful API built using Django and Django Rest Framework. It allows users to manage tasks by providing endpoints for creating, reading, updating, and deleting tasks. The API employs JWT (JSON Web Token) authentication for user security and includes Swagger for API documentation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

## Installation

To set up and run the Task Management System API on your local machine, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/altaf7740/task_management_system.git
   cd task_management_system
   ```
2. Create and activate virtual environment
   ```
   python3 -m venv env
   source evn/bin/activate
   ```
3. Install the required dependencies
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. python manage.py createsuperuser
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

To interact with the Task Management System API, you can use cURL commands, API clients, or test the endpoints using the Swagger documentation.

## API Endpoints
The following API endpoints are available:

- POST /api/token/: Obtain a JWT token by providing username and password.
- POST /api/token/refresh/: Refresh an existing JWT token.
- GET /api/tasks/: Retrieve a list of all tasks.
- GET /api/tasks/<task_id>/: Retrieve a specific task.
- POST /api/tasks/: Create a new task.
- PUT /api/tasks/<task_id>/: Update a task.
- PATCH /api/tasks/<task_id>/: Partially update a task.
- DELETE /api/tasks/<task_id>/: Delete a task.

## Authentication
The API uses JWT authentication for user security. Obtain a JWT token by sending a POST request to /api/token/ with your username and password.

```
curl -X POST -H "Content-Type: application/json" -d '{
  "username": "your_username",
  "password": "your_password"
}' http://localhost:8000/api/token/
```

## API Documentation
API documentation is available using Swagger. Access the documentation at http://localhost:8000/swagger/ when the development server is running.
