# print a list of calculator operations/functions
print("Operations:")
print("+ = Add")
print("- = Subtract")
print("* = Multiply")
print("/ = Divide")
print("^ = Power of")
print("\nANS = Previous answer")

result = 0

# create calculator function
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Cannot divide by 0!")
        return a / b
    elif op == '^':
        return a ** b


while True:
    # to allow multiple numbers to be entered, create a tuple here, e.g numbers = []
    # add a function to follow BODMAS

    # get user input
    a = (input('\nEnter first number: '))
    if a == "ANS":
        a = result
    else:
        a = float(a)
    op = input("Enter operation: (+, -, *, /, ^) ")
    b = (input('Enter second number (or "ANS" to use previous result): '))
    if b == "ANS":
        b = result
    else:
        b = float(b)

    # check that op is within the operations
    if op in "+-*/^":
        print(a, op, b)
        try:
            result = calculate(a, b, op)
            print('=', result)
        except ValueError as e:
            print("Error:", e)

        # ask user if they want to continue
        next_calculation = input("\nWould you like to do another calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Error: Invalid operation: {}".format(op))
