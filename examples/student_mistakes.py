# Common mistakes students make in Python

# 1. Indentation errors
def calculate_average(numbers):
for num in numbers:  # Missing indentation
    total += num
return total / len(numbers)  # Missing indentation

# 2. Variable scope issues
def process_list():
    numbers = [1, 2, 3]

print(numbers)  # Using variable outside scope

# 3. Import errors
from pandas import Series  # Trying to use package not in requirements
my_data = Series([1,2,3])
