# User Registration and Authentication System

## Overview

This project is a simple user registration and authentication system built using Flask, SQLite, and bcrypt for password hashing. The system allows users to register with a unique username and a securely hashed password. Registered users can then log in using their credentials to access user-specific page. The system implements session management to keep track of authenticated users.

## Features

- **User Registration**
  - Users can register with a unique username and password.
  - Passwords are securely hashed using bcrypt before storing in the database.

- **User Authentication**
  - Registered users can log in with their credentials.
  - Password validation is performed by comparing the hashed password retrieved from the database with the user-provided password using bcrypt.

- **Session Management**
  - Session-based authentication is implemented using Flask's session object.
  - Authenticated users can access user-specific content (e.g., user profile page).

- **Database Integration**
  - SQLite database is used to store user credentials (username and hashed password).
  - SQLAlchemy is not used in this project to keep it simple and lightweight.

- **Error Handling**
  - Error handling is implemented to manage invalid inputs and potential exceptions during registration and login processes.

## Limitations

- **Single User Session:**
  The system currently supports only one active session per user at a time.

- **Basic Error Handling:**
  Error handling is implemented at a basic level and may not cover all potential edge cases.

- **Minimal Frontend:**
  The frontend is simplistic and lacks advanced features like form validation or UI enhancements.

- **SQLite Limitations:**
  SQLite is used as a lightweight database, suitable for small-scale applications. For larger applications, a more robust database solution might be required.

- **Security Considerations:**
  While bcrypt is used for password hashing, additional security measures like rate limiting, CSRF protection, and HTTPS implementation should be considered for production deployments.

## Contributing
  Contributions to enhance the system or improve documentation are welcome. Please submit pull requests or raise issues for discussion.

This README.md file provide an overview of the project structure, features, setup instructions, and limitations. Feel free to customize and expand these documents based on your specific project requirements and deployment scenarios.

