num1 = int(input("Give me a number "))
num2 = int(input("Give me another "))
operation = input("Please specify if you'd like to "
                  "multiply, add, subtract or divide ")
try:
    if "multiply" in operation:
        print(num1 * num2)
    elif "add" in operation:
        print(num1+num2)
    elif "subtract" in operation:
        print(num1-num2)
    elif "divide" in operation:
        print(num1/num2)
finally:
    print("Hope you liked the calculator!")


