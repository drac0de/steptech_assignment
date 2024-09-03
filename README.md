# steptech_assignment

# Flask User Management App

## Overview
This is a simple Flask application that manages users. It connects to a MySQL database and allows for adding, viewing, and retrieving users.

## Setup Instructions

### Prerequisites
- Python 3.x
- Flask
- MySQL

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/drac0de/steptech_assignment.git
   cd steptech_assignment
   ```
2. Create a Virtual Environment(Optional)
    ```
    python -m venv venv
    source venv/bin/activate
    ```
3. Install Dependencies
    ```
    pip install -r requirements.txt
    ```

### Database Setup

1. Create a new database named "users"
2. Create a new table named "users" with columns id, name, email and role
3. Insert sample data.
    ```
    USE users;
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        role VARCHAR(255)
    );
    INSERT INTO users (name, email, role) VALUES ('Amit Sharma', 'amit.sharma@example.com', 'Admin');
    INSERT INTO users (name, email, role) VALUES ('Priya Singh', 'priya.singh@example.com', 'Moderator');
    INSERT INTO users (name, email, role) VALUES ('Ravi Kumar', 'ravi.kumar@example.com', 'Moderator');
    INSERT INTO users (name, email, role) VALUES ('Anjali Verma', 'anjali.verma@example.com', 'User');
    INSERT INTO users (name, email, role) VALUES ('Suresh Patel', 'suresh.patel@example.com', 'User');
    ```

### Github Workflow

Fork and clone the repository before performing the below steps:-

1. Branching<br/>
    Create a new branch for each feature or a bug fix.
    ```
    git checkout -b <branch-name>
    ```
2. Commiting and Pushing Changes<br/>
    Commit changes with a descriptive message.
    ```
    git add .
    git commit -m "Your descriptive message"
    git push
    ```
3. Creating a Pull Request<br/>
    Go to the repository on Github and create a pull request from your branch to the main branch.

### Queries Used

1. Insert sample data into the "users" table.
    ```
    INSERT INTO users (name, email, role) VALUES (%s, %s, %s);
    ```
2. Retrieve all users from the "users" table.
    ```
    SELECT * FROM users;
    ```
3. Retrieve a specific user by their ID.
    ```
    SELECT * FROM users WHERE id = %s;
    ```