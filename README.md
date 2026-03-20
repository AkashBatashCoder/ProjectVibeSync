# ProjectVibeSync

ProjectVibeSync is a simple social media web application built with Flask. Users can register, log in, create posts, edit their own posts, and delete them. The project is inspired by the Flask tutorial app, with UI and project-specific modifications.

## Features

- User registration and login
- Session-based authentication
- Create, update, and delete posts
- SQLite database for simple local storage
- Custom 404 page
- Flask app factory structure
- Blueprint-based routing

## Project Structure

```text
ProjectVibeSync/
├── flaskr/
│   ├── __init__.py
│   ├── auth.py
│   ├── blog.py
│   ├── db.py
│   ├── schema.sql
│   ├── static/
│   └── templates/
└── instance/
```

## Tech Stack

- Python
- Flask
- SQLite
- Jinja2
- Werkzeug

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AkashBatashCoder/FunProjectWithFlask.git
cd FunProjectWithFlask
```

If you have renamed the repository locally, enter that folder instead.

### 2. Create and activate a virtual environment

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
flask --app flaskr init-db
```

This creates the SQLite database inside the `instance/` folder.

### 5. Run the application

```bash
flask --app flaskr run
```

Then open the local address shown in your terminal.

## Configuration

The app uses Flask's app factory pattern. Database configuration is defined in `flaskr/__init__.py`.

Default database path:

```python
DATABASE = os.path.join(app.instance_path, "flaskr.sqlite")
```

Default secret key is currently set for development. Before any real public use, change it in your configuration.

## Available Routes

### Authentication
- `/auth/register` — register a new user
- `/auth/login` — log in
- `/auth/logout` — log out

### Blog
- `/` — home page with posts
- `/create` — create a new post
- `/<id>/update` — edit a post
- `/<id>/delete` — delete a post

## Development Notes

- Only the author of a post can edit or delete it.
- The database is initialized from `flaskr/schema.sql`.
- The app uses Flask blueprints for separation of concerns.

## Deployment Notes

For simple testing deployment on platforms like PythonAnywhere:

1. Upload or clone the project
2. Create a virtual environment
3. Install dependencies
4. Run:

```bash
flask --app flaskr init-db
```

5. Configure the WSGI file to import the app factory:

```python
from flaskr import create_app
application = create_app()
```

## Future Improvements

- Better form validation
- Profile pages
- Image upload support
- Likes and comments
- Production configuration with environment variables
- Replace SQLite with PostgreSQL or MySQL for scaling

## License

This project is for learning and experimentation.
