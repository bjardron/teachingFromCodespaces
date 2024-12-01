# Exercise 4: Fixing Mistakes
# Learn how to recover from common Git problems

"""
Task 1: Undoing Uncommitted Changes
1. Make some changes to this function
2. To undo changes in one file:
   - Source Control panel -> right click -> Discard Changes
   - Or in terminal: git checkout -- filename
3. To undo all changes:
   - Source Control panel -> Discard All Changes
   - Or in terminal: git reset --hard
"""
def example_function():
    return "Make some changes here"

"""
Task 2: Oops, Wrong Branch!
If you committed to main instead of a feature branch:
1. Create new branch where you are:
   git checkout -b feature-branch
2. Move back to main:
   git checkout main
3. Reset main to before your commit:
   git reset --hard HEAD~1
"""

"""
Task 3: Recovering Deleted Code
1. Delete some code from this function
2. File -> Undo (Ctrl/Cmd + Z) works if you just deleted
3. If you saved after deleting:
   - Source Control -> right click -> Discard Changes
4. If you committed the deletion:
   - git reset --hard HEAD~1 to undo last commit
"""
def dont_delete_me():
    print("Some important code here")
    print("More important code")
    return "Critical function"

"""
Task 4: Codespaces Troubleshooting
Common issues and fixes:

1. Codespace won't load:
   - Try: Reload window (Ctrl/Cmd + R)
   - Try: Create new codespace
   - Check: GitHub status page

2. Can't save/sync:
   - Check internet connection
   - Try: Source Control panel manual sync
   - Check: GitHub access/permissions

3. Extensions not working:
   - Reload window
   - Reinstall extension
   - Check extension settings
"""

# Practice area - make some changes here and try recovering from them!
def practice_area():
    # Try:
    # 1. Making changes and undoing them
    # 2. Deleting code and recovering it
    # 3. Committing and undoing the commit
    pass
