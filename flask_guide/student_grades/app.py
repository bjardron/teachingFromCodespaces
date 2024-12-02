# Import necessary modules from Flask
# Flask: The core web framework
# render_template: For displaying HTML files
# request: For handling form submissions
from flask import Flask, render_template, request

# Create a Flask application instance
# __name__ is a special Python variable that tells Flask where to find files
app = Flask(__name__)

# Create an empty list to store our student data
# In a real application, this would be a database
students = []

# Define our route - this tells Flask what URL to listen to
# '/' means the root URL (homepage)
# methods=['GET', 'POST'] allows both viewing the page (GET) and submitting forms (POST)
@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if someone submitted the form (POST request)
    if request.method == 'POST':
        # Get data from the form
        # request.form works like a dictionary of form data
        name = request.form.get('name')
        grade = request.form.get('grade')
        
        # Only add to our list if both name and grade were provided
        if name and grade:
            # Convert grade to integer and store both in a dictionary
            students.append({'name': name, 'grade': int(grade)})
    
    # Calculate the class average
    # We use a ternary operator here:
    # - If students list is empty, average is 0
    # - If we have students, calculate the average
    average = sum(s['grade'] for s in students) / len(students) if students else 0
    
    # Display the page with our data
    # render_template looks in the templates folder
    # We pass our variables to the template
    return render_template('index.html', students=students, average=average)

# This checks if we're running this file directly (not importing it)
if __name__ == '__main__':
    # Start the Flask development server
    # debug=True enables error messages and auto-reload
    app.run(debug=True)
