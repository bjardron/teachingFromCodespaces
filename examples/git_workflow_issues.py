"""
Common Git workflow issues:

1. Working directly in main
def new_feature():
    # This should be in a branch
    pass

2. Multiple people editing same file without pulling
# Person A's version
def process_data():
    return "A's changes"

# Person B's version (will cause conflict)
def process_data():
    return "B's changes"

3. Commit messages
# Bad commits:
# "changes"
# "fix"
# "asdfgh"
# "final version"
# "final version 2"
"""
