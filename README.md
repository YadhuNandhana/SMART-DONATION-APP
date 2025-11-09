# Smart Donation & Resource Redistribution System (Django Backend MVP)

This project implements the backend for a Smart Donation & Resource Redistribution System using Django REST Framework. The frontend (React.js) setup has been skipped due to local environment issues.

## Features Implemented (Backend)

*   **User Authentication:** JWT-based login for Donor, NGO, and Volunteer roles.
*   **Core Modules:**
    *   **Donor:** User registration, profile management, donation creation (with auto-suggestion of nearest NGOs).
    *   **NGO:** Profile management, needs list management.
    *   **Volunteer:** Profile management.
*   **Donation Management:** Create, retrieve, update, delete donations. Includes expiry alerts and status tracking.
*   **Pickup Management:** Create, retrieve, update, delete pickup requests.
*   **NGO Verification:** Admin panel for NGO verification (DARPAN ID input + status flag).
*   **Location-based Matching:** Haversine distance calculation to find nearest verified NGOs for donations.
*   **Basic Analytics:** Dashboard view for total donations, redistributed items, donations by category, and active NGOs.
*   **Admin Panel:** Custom admin interface for managing users, profiles, donations, and NGO verifications.

## Tech Stack (Backend)

*   **Backend:** Django REST Framework (Python 3.12)
*   **Database:** SQLite
*   **Auth:** JWT-based login (djangorestframework-simplejwt)

## Setup Instructions

Follow these steps to set up and run the Django backend:

### 1. Navigate to the Project Directory

```bash
cd smart-donation-app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
.\venv\Scripts\python.exe -m pip install django djangorestframework django-cors-headers djangorestframework-simplejwt
```

### 4. Database Configuration (SQLite)

This project is configured to use SQLite, which is a file-based database and requires no additional setup. The database file `db.sqlite3` will be created automatically in the project root when you run migrations.

### 5. Run Migrations

Apply the database migrations to create the necessary tables:

```bash
.\venv\Scripts\python.exe manage.py makemigrations
.\venv\Scripts\python.exe manage.py migrate
```

### 6. Create a Superuser (for Admin Panel access)

```bash
.\venv\Scripts\python.exe manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 7. Run the Development Server

```bash
.\venv\Scripts\python.exe manage.py runserver
```
The Django backend will be running at `http://127.0.0.1:8000/`.

### 8. Access the Admin Panel

You can access the Django Admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials you created.

### 9. Deployment on Render

To deploy this Django backend on Render, follow these steps:

**a. Create a `requirements.txt` file:**
Ensure you have a `requirements.txt` file in your project root (or `smart_donation_backend` directory) with all Python dependencies, including `gunicorn`. A sample `requirements.txt` is provided in `smart_donation_backend/requirements.txt`.

**b. Create an `.env` file:**
Create a `.env` file in your project root (or `smart_donation_backend` directory) based on the `.env.example` template. Fill in your actual secret key and allowed hosts.

**c. Render Configuration:**
When setting up your web service on Render, use the following commands:

*   **Build Command:**
    ```bash
    pip install -r requirements.txt
    ```
*   **Start Command:**
    ```bash
    gunicorn smart_donation_backend.wsgi:application --bind 0.0.0.0:$PORT
    ```
    Ensure your `Procfile` (if you create one) also specifies this start command.

**d. Environment Variables on Render:**
Add the environment variables from your `.env` file to your Render service settings.

### 10. API Endpoints

*   **User Registration:** `/api/donor/register/` (POST)
*   **User Login (JWT):** `/api/donor/login/` (POST)
*   **Refresh Token:** `/api/donor/login/refresh/` (POST)
*   **Donor Profile:** `/api/donor/profile/` (GET, PUT, PATCH)
*   **Current User Details:** `/api/donor/user/` (GET)
*   **NGO Profiles:** `/api/ngo/profiles/` (GET, POST)
*   **My NGO Profile:** `/api/ngo/profiles/me/` (GET, PUT, PATCH, DELETE)
*   **Specific NGO Profile:** `/api/ngo/profiles/<int:pk>/` (GET, PUT, PATCH, DELETE)
*   **NGO Needs:** `/api/ngo/needs/` (GET, POST)
*   **Specific NGO Need:** `/api/ngo/needs/<int:pk>/` (GET, PUT, PATCH, DELETE)
*   **Volunteer Profiles:** `/api/volunteer/profiles/` (GET, POST)
*   **My Volunteer Profile:** `/api/volunteer/profiles/me/` (GET, PUT, PATCH, DELETE)
*   **Specific Volunteer Profile:** `/api/volunteer/profiles/<int:pk>/` (GET, PUT, PATCH, DELETE)
*   **Donations:** `/api/donations/` (GET, POST)
*   **Specific Donation:** `/api/donations/<int:pk>/` (GET, PUT, PATCH, DELETE)
*   **Expiring Donations:** `/api/donations/expiring/` (GET)
*   **Nearest NGOs for a Donation:** `/api/donations/<int:pk>/nearest-ngos/` (GET)
*   **Analytics Dashboard:** `/api/donations/analytics/` (GET)
*   **NGO Verifications:** `/api/verification/` (GET, POST)
*   **Specific NGO Verification:** `/api/verification/<int:pk>/` (GET, PUT, PATCH, DELETE)

## Frontend (Skipped)

The React frontend setup was skipped due to persistent issues with Node.js/npm environment on the local machine. If you wish to set up the frontend, you would typically:

1.  Navigate to the `smart-donation-app` directory.
2.  Run `npx create-react-app frontend` (after ensuring Node.js and npm are correctly installed and in PATH).
3.  Install necessary frontend dependencies (e.g., `axios`, `react-router-dom`, UI library).
4.  Implement authentication, role-based dashboards, forms, and integrate with the Django backend APIs.
5.  Apply the specified UI/UX styling.
