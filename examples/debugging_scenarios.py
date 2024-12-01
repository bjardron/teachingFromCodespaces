# Common debugging scenarios

def divide_numbers(a, b):
    try:
        return a/b
    except:  # Bad practice: catch-all except
        pass  # Silent failure

def process_age():
    age = input("Enter age: ")
    return age * 2  # No type conversion

def update_score(score_dict, player):
    score_dict[player] += 1  # KeyError if player doesn't exist

# File: solutions/debugging_fixed.py
def divide_numbers_fixed(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"Error: Invalid number format - {e}")
        return None

def process_age_fixed():
    try:
        age = int(input("Enter age: "))
        return age * 2
    except ValueError:
        print("Please enter a valid number")
        return None

def update_score_fixed(score_dict, player):
    score_dict.setdefault(player, 0)  # Initialize if doesn't exist
    score_dict[player] += 1
