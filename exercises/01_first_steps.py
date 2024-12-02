# Exercise 1: Your First GitHub Steps
# Follow along with each task to learn the basics of Git and Codespaces

"""
Task 1: Making Changes
- Edit the greet() function below to return "Hello, [name]!"
- Save the file
- Look at the Source Control panel (Ctrl/Cmd + Shift + G)
- Notice how Git shows you the changes
"""
def greet(name):
    return f"Hello, {name}!"

"""
Task 2: Committing Changes
After editing the function:
1. Click the + (Stage Changes) in the Source Control panel
2. Enter a descriptive commit message
3. Click the ✓ (Commit)
"""

"""
Task 3: Pushing to GitHub
After committing:
1. Click the ... menu in Source Control
2. Select 'Push'
3. See your changes appear on GitHub
"""

# Test your function here:
if __name__ == "__main__":
    print(greet("Teacher"))  # Should print: Hello, Teacher!
