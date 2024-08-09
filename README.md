
# Full-Stack Project Setup

## Overview

This project is a full-stack application consisting of:
- **Backend**: Django REST Framework
- **Frontend**: Angular
- **Database**: Mysql
- **Shared ORM Library**: Contains database models and migration, serializers and other entities
  
## Prerequisites

Make sure you have the following installed:
- Python 3.9+
- Node.js 16+
- Pip
- npm

## folder Structure

1. **Backend folder**: Django REST Framework backend code.
2. **Frontend folder**: Angular frontend code.
3. **Shared ORM Library folder**: Contains database models and migration files.

## Setup Instructions

### 1. Clone the Repositories

Clone the repositories to your local machine:

```bash
git clone <assessment-repo-url> 
```

### 1. Set Up the backend Project

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2.  create and activate a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. Install the backend dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    setup your Database default using configuration given below(remember do not change creds otherwise you need to change db Config in shared-orm library and install it your backend project)

    python manage.py migrate
    ```

5. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

   The backend will be accessible at `http://localhost:8000`.

### 4. Set Up the Frontend

1. Navigate to the `frontend` directory:

    ```bash
    cd frontend
    cd frontendapp
    ```

2. Install the frontend dependencies:

    ```bash
    npm install
    ```

3. Start the Angular development server:

    ```bash
    npm run start (use this command only)
    ```

   The frontend will be accessible at `http://localhost:4200`(if it will not run in normal chrome browser please use incognito mode as there might be an issue with cors header from backend which can restrict any API calls)

### 5. Configure mySQL

1. Ensure mySQL is installed and running.

2. Create a database named `My-account` using Dbeaver software or any other of your choice:

3. Verify and configure mySQL settings in the `shared_orm_library` if needed.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_account',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### 6. Verify the Setup

- **Backend**: Access the API at `http://127.0.0.1:8000/users/` to ensure it returns a list of users
- **Frontend**: Access the Angular application at `http://localhost:4200/user` and confirm it displays the user list fetched from the backend. (and it will display users in table form)

REMEBER TO ADD USER DATA in DATABASE MANUALLY

