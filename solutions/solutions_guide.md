# Workshop Solutions Guide

## Exercise Solutions

### Exercise 1: Basic Git Operations
```python
# Solution to 01_first_steps.py
def greet(name):
    return f"Hello, {name}!"

# Git commands used:
# 1. git add 01_first_steps.py
# 2. git commit -m "Implemented greeting function"
# 3. git push
```

### Exercise 2: Branching
```python
# Solution to 02_branching.py
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

# Branch commands used:
# 1. git checkout -b feature-calculator
# 2. git add 02_branching.py
# 3. git commit -m "Added calculator functions"
# 4. git push -u origin feature-calculator
```

### Exercise 3: Merge Conflicts
```python
# Solution to 03_merge_conflicts.py
def sort_numbers(numbers):
    """Solution that combines both requirements"""
    return {
        'ascending': sorted(numbers),
        'descending': sorted(numbers, reverse=True)
    }

# Resolving conflict steps:
# 1. git checkout main
# 2. git pull
# 3. git checkout feature-branch
# 4. git merge main
# 5. Fix conflicts
# 6. git add .
# 7. git commit -m "Resolved merge conflicts"
```

### Exercise 4: Fixing Mistakes
```python
# Common recovery scenarios

# 1. Undo last commit but keep changes
git reset --soft HEAD~1

# 2. Undo last commit and discard changes
git reset --hard HEAD~1

# 3. Recover deleted file
git checkout HEAD -- filename

# 4. Move commits to new branch
git branch new-branch
git reset --hard HEAD~1
git checkout new-branch
```

## Common Issues and Solutions

### Git Problems

1. Wrong Branch
```bash
# If you committed to main instead of a feature branch:
git checkout -b feature-branch  # Create new branch at current commit
git checkout main
git reset --hard HEAD~1        # Move main back
```

2. Bad Commit Message
```bash
# If you just made the commit:
git commit --amend -m "Better message"

# If commit was already pushed:
# (Only do this if others haven't pulled your changes)
git commit --amend -m "Better message"
git push --force-with-lease
```

3. Large Files Committed
```bash
# Remove file from git but keep locally
git rm --cached large_file
echo "large_file" >> .gitignore
git commit -m "Remove large file"
```

### Codespace Issues

1. Environment Problems
```bash
# Rebuild container
Command Palette (Ctrl/Cmd + Shift + P) -> Rebuild Container

# Reset environment
Delete codespace and create new one
```

2. Extension Issues
```bash
# Reset VS Code
Command Palette -> Reload Window

# Check extension logs
View -> Output -> Select extension from dropdown
```

### Code Problems

1. Debugging Python Errors
```python
# ImportError
# Check requirements.txt includes needed packages
# Run: pip install -r requirements.txt

# IndentationError
# Use VS Code's format document:
# Right click -> Format Document

# NameError
# Check variable scope
# Add needed imports
```

2. Testing Issues
```python
# Run specific test
python -m unittest test_file.py -k test_name

# Debug test
# Add breakpoint() in code
# Run test with -m pdb
```

## Best Practices

### Git Workflow
1. Always create branch for new features
2. Pull before starting new work
3. Commit often with clear messages
4. Push regularly to backup work

### Code Organization
1. Use clear file/folder structure
2. Keep related code together
3. Add README files
4. Include requirements.txt

### Teaching Tips
1. Start with simple examples
2. Build complexity gradually
3. Use real-world scenarios
4. Prepare for common issues

## Quick Reference

### Essential Git Commands
```bash
# Basic
git status
git add .
git commit -m "message"
git push

# Branches
git checkout -b branch-name
git merge branch-name
git push -u origin branch-name

# Fixes
git reset --hard HEAD~1
git checkout -- filename
git clean -fd
```

### VS Code Shortcuts
```
Ctrl/Cmd + S: Save
Ctrl/Cmd + Z: Undo
Ctrl/Cmd + Shift + P: Command Palette
Ctrl/Cmd + B: Toggle sidebar
Ctrl/Cmd + J: Toggle terminal
```
