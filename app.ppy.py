""" x = 3
y = float(3)
print(x,y)
 """



""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
print(values[0]) """

""" def is_odd_or_even(number):

    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    
    return "Even" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    try:
        # Get user input
        user_input = input("Enter an integer: ").strip()
        
        # Convert to integer
        num = int(user_input)
        
        # Determine and display result
        result = is_odd_or_even(num)
        print(f"{num} is {result}.")
    
    except ValueError as e:
        print(f"Error: {e}")
 """



""" service = input("How was the service?").capitalize
if service == "Great":
    print("25%")
elif service == "Good":
    print("20%")
elif service == "Okay":
    print("15%")
elif service == "Bad":
    print("0%")
    """

""" def find_factors(number):

    if not isinstance(number, int) or number <= 0:
        return "Invalid input: Please enter a positive integer."

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
num1 = 12
factors1 = find_factors(num1)
print(f"The factors of {num1} are: {factors1}") """


import math

def greatest_common_factor(a,b):
    while b:
        a, b = b, a % b
    return a
num1 = 58
num2 = 94
gcf = greatest_common_factor(num1, num2)
print(f"The greatest common factor between {num1} and {num2} is: {gcf}")