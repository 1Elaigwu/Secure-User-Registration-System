# Overview

This folder contains the backend code for the user registration and authentication system.

### Contents

- `app.py`: Flask application defining routes and database interactions.
- `user_database.db`: SQLite database file storing user credentials.

### Setup

1. Install Python and Flask framework.
2. Install required packages using `pip install -r requirements.txt`.
3. Run `app.py` to start the Flask application.

### Dependencies

- Python 3.x
- Flask
- bcrypt

### Database Schema

The database schema consists of a single table `users`:

- `username`: TEXT (unique, primary key)
- `password`: TEXT (hashed password)

### Notes

- Make sure to set a secure secret key for Flask session management.
- Update database configurations (e.g., database path) as needed in `app.py`.
