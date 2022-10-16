#M G Juriss
# Basic Calculator

# On-screen insruction with options
print("Select an operation to perform:")
print("1.  ADD")
print("2.  SUBTRACT")
print("3.  MULTIPLY")
print("4.  DIVIDE")

# set the input function
operation = input()

if operation  == "1":
    # code for ADD
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("the sum is " + str(int(num1) + int(num2)) + ".")

    if operation  == "2":
    # code for SUBTRACT
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("the sum is " + str(int(num1) - int(num2)) + ".")

    if operation  == "3":
    # code for MULTIPLY
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("the sum is " + str(int(num1) x int(num2)) + ".")

    if operation  == "4":
    # code for DIVIDE
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("the sum is " + str(int(num1) / int(num2)) + ".")