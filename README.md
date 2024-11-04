# User Registration Application with Python-Tkinter and MySQL

This is a graphical user interface (GUI) application for registering users and storing their information in a MySQL database. Built using Python's Tkinter library, the application features a registration form that captures a user's name, age, course, and course duration. All registered users' data is saved in a MySQL database and can be viewed in the application.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [License](#license)

## Features
- **User Registration Form**: Allows users to input their name, age, course, and duration.
- **Database Integration**: Stores user data in a MySQL database with an `id`, `name`, `age`, `course`, and `duration`.
- **Data Display**: Shows registered users in a list with details formatted for readability.
- **Responsive Design**: GUI elements adjust to provide a user-friendly experience.

## Prerequisites
- **Python 3.x**
- **MySQL Server** (ensure that it's installed and running on your system)
- **MySQL Connector for Python**: Install using `pip` if it's not already installed.

## Installation
1) **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name

## 2) Install Required Python Packages: Install the MySQL connector for Python using pip.

```bash
pip install mysql-connector-python
```
## 3) Set Up MySQL Database: Make sure MySQL server is running and create a database for this application, such as user_registration_db. See Database Setup below.

## 4) Database Setup
Create the Database: Log in to MySQL and create a new database for user registrations.

sql
```bash
CREATE DATABASE user_registration_db;
```
Update Database Connection in Code: Ensure your MySQL credentials are correct in the code (host, user, password, database).
Create Users Table: The application automatically creates a users table if it does not already exist. This is done by the connect_db() function, which is called when the application starts.

## Running the Application
Run the Python script to start the application.

```bash
python your_script_name.py
```
## Project Structure
connect_db(): Initializes the database and creates the users table if it doesn’t exist.
register_user(): Handles user registration and inserts new records into the MySQL database.
view_users(): Fetches and displays all registered users from the database in a formatted list.
## Usage
Registering a User:

Enter user information (name, age, course, duration).
Click on the Register button to save the data to the database.
A success message will display on successful registration.
Viewing Registered Users:

Click on View Users to see a list of all registered users in a structured format with headers.
The list includes fields: Name, Age, Course, and Duration.
