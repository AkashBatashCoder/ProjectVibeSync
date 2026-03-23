import os 

from flask import Flask, app, flash, render_template, request
from flask import g, redirect, url_for
from flask_wtf.csrf import CSRFProtect, CSRFError


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    #ensure that the instance path exists
    os.makedirs(app.instance_path, exist_ok=True)
    
    

    # Initialize CSRF protection
    csrf = CSRFProtect(app)
    csrf.init_app(app)


    # @app.route('/')
    # def home():
    #     return "This is the simple home page."

    # @app.route('/hello')
    # def hello():
    #     return "Hello world! This is Hello page"

    # Initialize the database
    from . import db
    db.init_app(app)

    # Register the auth blueprint for auth  
    from . import auth
    app.register_blueprint(auth.bp)

    # Register the blog blueprint for blog
    from . import blog
    app.register_blueprint(blog.bp)

    #app.add_url_rule('/', endpoint='index')
    @app.route('/')
    def home():
        if g.get('user'):
            return redirect(url_for('blog.index'))
        return render_template('home.html')

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404
    
    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        flash("The form has expired. Please try again.", "danger")
        return redirect(request.url), 302

    return app
    
