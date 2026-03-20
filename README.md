# ProjectVibeSync

ProjectVibeSync is a simple social media web application built with Flask.  
It is inspired by the official Flask tutorial app, but includes custom changes and UI modifications.

Users can:

- Register for an account
- Log in and log out
- Create posts
- Edit their own posts
- Delete their own posts
- View posts from all users

## Tech Stack

- Python
- Flask
- SQLite
- Jinja2 templates
- HTML / CSS

## Project Structure

```text
ProjectVibeSync/
├── VibeSync/
│   ├── __init__.py
│   ├── auth.py
│   ├── blog.py
│   ├── db.py
│   ├── schema.sql
│   ├── static/
│   └── templates/
├── instance/
├── requirements.txt
├── .gitignore
└── README.md
```

## Features

- User authentication
- Session-based login system
- CRUD operations for posts
- SQLite database for testing and local development
- Flask application factory pattern

## How to Run Locally

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ProjectVibeSync
```

### 2. Create and activate a virtual environment

#### Linux / macOS
```bash
python -m venv env
source env/bin/activate
```

#### Windows
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
flask --app VibeSync init-db
```

### 5. Run the application

```bash
flask --app VibeSync run
```

For debug mode:

```bash
flask --app VibeSync --debug run
```

The app will usually be available at:

```text
http://127.0.0.1:5000
```

## Database

This project currently uses SQLite for simplicity and testing.

The database file is created inside the `instance/` folder when you run:

```bash
flask --app VibeSync init-db
```

## Notes

- This project is for learning and testing purposes.
- SQLite is being used intentionally for now.
- The app follows the Flask app factory pattern.

## Future Improvements

Possible future improvements:

- Profile pages
- Image upload support
- Comments and reactions
- Better form validation
- Production deployment configuration

## License

This project is for educational and personal learning purposes.