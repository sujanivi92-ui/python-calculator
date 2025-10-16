# ==============================================
# Simple Calculator
# Concepts: input(), variables, datatypes, operators, f-string, if-else
# ==============================================

# Get user input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

# Perform calculation based on operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Handle division by zero
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
elif operator == '%':
    result = num1 % num2
else:
    result = "Invalid operator!"

# Display result
print("\n========== CALCULATOR RESULT ==========")
print(f"{num1} {operator} {num2} = {result}")
print("=======================================")
