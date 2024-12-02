# Building a Student Grade Tracker with Flask
## Step-by-Step Guide

### Setup (5 mins)
1. In your Codespace:
   ```bash
   # Create project folder
   mkdir student_grades
   cd student_grades
   
   # Create required files/folders
   mkdir templates static
   touch app.py requirements.txt
   touch templates/index.html
   touch static/style.css
   ```

2. Add to requirements.txt:
   ```
   Flask==3.0.0
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Step 1: Create Basic App (10 mins)
1. In app.py, add basic Flask setup:
   ```python
   from flask import Flask, render_template
   
   app = Flask(__name__)
   
   @app.route('/')
   def index():
       return render_template('index.html')
   
   if __name__ == '__main__':
       app.run(debug=True)
   ```

2. Create basic template in templates/index.html:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Grade Tracker</title>
   </head>
   <body>
       <h1>Student Grade Tracker</h1>
   </body>
   </html>
   ```

3. Test your app:
   ```bash
   python app.py
   ```
   Click the link when Codespaces forwards the port.

### Step 2: Add Form (10 mins)
1. Update index.html with a form:
   ```html
   <form method="POST">
       <input type="text" name="name" placeholder="Student Name" required>
       <input type="number" name="grade" placeholder="Grade" required>
       <button type="submit">Add Grade</button>
   </form>
   ```

2. Update app.py to handle form:
   ```python
   from flask import Flask, render_template, request
   
   app = Flask(__name__)
   students = []  # Store grades here
   
   @app.route('/', methods=['GET', 'POST'])
   def index():
       if request.method == 'POST':
           name = request.form.get('name')
           grade = request.form.get('grade')
           if name and grade:
               students.append({'name': name, 'grade': int(grade)})
       return render_template('index.html', students=students)
   ```

### Step 3: Display Data (10 mins)
1. Add table to index.html:
   ```html
   <table>
       <tr>
           <th>Name</th>
           <th>Grade</th>
       </tr>
       {% for student in students %}
       <tr>
           <td>{{ student.name }}</td>
           <td>{{ student.grade }}</td>
       </tr>
       {% endfor %}
   </table>
   ```

### Step 4: Add Styling (10 mins)
1. In static/style.css:
   ```css
   body {
       font-family: Arial;
       max-width: 800px;
       margin: 0 auto;
       padding: 20px;
   }
   
   table {
       width: 100%;
       border-collapse: collapse;
   }
   
   th, td {
       padding: 8px;
       border: 1px solid #ddd;
   }
   ```

2. Link CSS in index.html:
   ```html
   <head>
       <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
   </head>
   ```

### Step 5: Add Average Calculation (5 mins)
1. Update app.py:
   ```python
   @app.route('/', methods=['GET', 'POST'])
   def index():
       if request.method == 'POST':
           name = request.form.get('name')
           grade = request.form.get('grade')
           if name and grade:
               students.append({'name': name, 'grade': int(grade)})
       
       average = sum(s['grade'] for s in students) / len(students) if students else 0
       return render_template('index.html', students=students, average=average)
   ```

2. Display average in index.html:
   ```html
   {% if students %}
       <p>Class Average: {{ average|round(2) }}</p>
   {% endif %}
   ```

### Running the App
1. Make sure you're in the right directory
2. Run: `python app.py`
3. Click the forwarded port link in Codespaces
4. Try adding some grades!

### Common Issues
- If page isn't updating, check 'debug=True' in app.py
- If form isn't working, check method="POST" in form tag
- If styling isn't loading, check CSS file path
- If average shows error, check for empty students list

### Extensions (If Time Permits)
1. Add delete button for grades
2. Add grade validation (0-100)
3. Add sorting by name or grade
4. Show highest/lowest grades
