# Exercise 2: Working with Branches
# Learn how to create and manage branches in Git

"""
Task 1: Creating a Branch
1. In the bottom left of VS Code, click where it says 'main'
2. Click 'Create new branch'
3. Name it 'feature-calculator'
4. Notice how the bottom left now shows your new branch name
"""

"""
Task 2: Making Changes in Your Branch
Implement the Calculator class below with new methods
"""
class Calculator:
    def add(self, a, b):
        return a + b
    
    # TODO: Implement subtract method
    def subtract(self, a, b):
        pass
    
    # TODO: Implement multiply method
    def multiply(self, a, b):
        pass

"""
Task 3: Committing Branch Changes
1. Stage your changes (+ icon in Source Control)
2. Commit with a message like "Added calculator functions"
3. Push your branch using the sync/push button
"""

"""
Task 4: Creating a Pull Request (PR) from Codespaces
Method 1 - Source Control Panel:
1. After pushing, click the 'Create Pull Request' button in Source Control
2. This opens GitHub UI in a new tab
3. Fill in PR details and create

Method 2 - GitHub UI in Codespaces:
1. Click the GitHub icon in the left sidebar (looks like a cat)
2. Find 'Pull Request' section
3. Click '+' to create new PR
4. Select your branch to merge into main
5. Fill in details and create

Method 3 - Command Palette:
1. Press Ctrl/Cmd + Shift + P
2. Type 'Pull Request'
3. Select 'Create Pull Request'
4. Follow the prompts
"""

# Test your functions here:
if __name__ == "__main__":
    calc = Calculator()
    print("Testing add:", calc.add(5, 3))      # Should print 8
    print("Testing subtract:", calc.subtract(5, 3))  # Should print 2
    print("Testing multiply:", calc.multiply(5, 3))  # Should print 15
