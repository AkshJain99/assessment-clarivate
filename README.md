
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

### 2. Set Up the Shared ORM Library

1. Navigate to the `shared-orm-library` directory:

    ```bash
    cd shared-orm-library
    ```

2. Install the shared ORM library:

    ```bash
    pip install -e .
    ```

   This installs the `shared_orm_library` package in editable mode, allowing you to make changes and see them immediately.

### 3. Set Up the Backend

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. Install the backend dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
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
    ```

2. Install the frontend dependencies:

    ```bash
    npm install
    ```

3. Start the Angular development server:

    ```bash
    ng serve
    ```

   The frontend will be accessible at `http://localhost:4200`.

### 5. Configure PostgreSQL

1. Ensure PostgreSQL is installed and running.

2. Create a database named `My-account`:

    ```sql
    CREATE DATABASE "My-account";
    ```

3. Verify and configure PostgreSQL settings in the `shared_orm_library` if needed.

### 6. Verify the Setup

- **Backend**: Access the API at `http://localhost:8000/users/` to ensure it returns a list of users.
- **Frontend**: Access the Angular application at `http://localhost:4200/` and confirm it displays the user list fetched from the backend.

## Troubleshooting

- **ModuleNotFoundError**: If you encounter issues importing `shared_orm_library`, ensure the path is correctly added to `sys.path` in your Django settings.
- **Database Issues**: Check PostgreSQL service status and ensure the database name and credentials are correct in the `shared_orm_library`.

## Contributing

To contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the URLs and paths according to your project specifics. If you need further modifications or additional sections, just let me know!
