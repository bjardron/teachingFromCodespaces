# Exercise 3: Handling Merge Conflicts
# Learn how to create, understand, and resolve merge conflicts

"""
Task 1: Setting Up the Conflict
1. Create two branches from main:
   - Branch 1: feature-list-ascending
   - Branch 2: feature-list-descending

2. We'll make different changes to this function in each branch!
"""
def sort_numbers(numbers):
    # This function will be modified differently in each branch
    return numbers

"""
Task 2: Making Conflicting Changes
1. In feature-list-ascending branch:
   - Modify the function to sort numbers in ascending order
   - Commit and push

2. Switch to feature-list-descending branch:
   - Modify the SAME function to sort in descending order
   - Commit and push
"""

"""
Task 3: Creating the Conflict
1. Create a PR from feature-list-ascending to main
2. Merge it
3. Create a PR from feature-list-descending to main
4. Notice the conflict!
"""

"""
Task 4: Resolving the Conflict
When you see the conflict, you'll notice markers like:
<<<<<<< HEAD
your code
=======
their code
>>>>>>> feature-branch

1. Decide which code to keep (or combine them)
2. Remove the conflict markers
3. Commit the resolution
4. Complete the PR
"""

# Test your function here:
if __name__ == "__main__":
    numbers = [4, 2, 7, 1, 9, 3]
    print("Original:", numbers)
    print("Sorted:", sort_numbers(numbers))
