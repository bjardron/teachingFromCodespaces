# Introduction to Flask

## What is Flask?
Flask is a lightweight web application framework for Python. Think of it as a toolkit for building web applications. It's called a "micro" framework because it provides the essentials while keeping the core simple and extensible.

## Why Use Flask?
1. Simple to learn and use
2. Perfect for teaching web development
3. Built-in development server
4. Easy to extend with additional features
5. Great for both small projects and scalable applications

## Common Uses
- Web Applications
- APIs (Application Programming Interfaces)
- Educational projects
- Prototypes and MVPs (Minimum Viable Products)
- Backend for JavaScript applications
- Data visualization dashboards

## Basic Concepts

### 1. Routes
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "About page"
```

### 2. Templates
```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

### 3. HTTP Methods
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return handle_login()
    else:
        return show_login_form()
```

## Getting Started

### Basic Setup
```python
# Install Flask
pip install flask

# Create app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Project Structure
```
my_flask_app/
├── app.py
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   ├── css/
│   └── js/
└── requirements.txt
```

## Key Features

### 1. URL Building
```python
from flask import url_for

@app.route('/user/<username>')
def user_profile(username):
    return f"Profile of {username}"
```

### 2. Request Handling
```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    return f"Received: {data}"
```

### 3. File Uploads
```python
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploaded_file.txt')
```

### 4. Sessions
```python
from flask import session

@app.route('/login')
def login():
    session['username'] = 'user123'
```

## Best Practices

1. Project Organization
   - Use blueprints for larger applications
   - Separate concerns (views, models, etc.)
   - Keep configuration in separate files

2. Security
   - Use CSRF protection
   - Sanitize user input
   - Secure session handling

3. Development
   - Use debug mode during development
   - Implement proper error handling
   - Write tests for your routes

## Common Patterns

### 1. Form Handling
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NameForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')
```

### 2. Database Integration
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
```

### 3. Authentication
```python
from flask_login import LoginManager, UserMixin

login_manager = LoginManager()
login_manager.init_app(app)
```

## Debugging Tips

1. Debug Mode
   ```python
   app.run(debug=True)
   ```

2. Logging
   ```python
   app.logger.debug('Debug message')
   app.logger.error('Error message')
   ```

3. Error Pages
   ```python
   @app.errorhandler(404)
   def not_found(e):
       return render_template('404.html'), 404
   ```

## Resources
- Official Documentation: https://flask.palletsprojects.com/
- Flask Extensions: https://flask.palletsprojects.com/en/3.0.x/extensions/
- Flask Mega-Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
