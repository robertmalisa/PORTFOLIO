# saying hello to the user
def calculator_1():
    print("hello there!")
    first_name = input("what is your first name: ").strip().upper()
    last_name = input("what is your sur name: ").strip().upper()
    print("hi " + first_name + " " + last_name + "welcome to this app\n you can add, less , divide, square,and multiply")

    while True:
           try:
               num1 = float(input("Enter the number: "))
           except ValueError:
               print("please enter a number!")
           else:
                break

    o = input(" select the operator, either '+', '-', 'x', '**' or '/': ")
    if o == '**':
        print("the square of " + str(num1) + " is,")
        print(num1 ** 2)
    else:
        while True:
            if o in ["+", "-", "*", "/"]:
                break
            else:
                print("please put a valid operator!")
                continue

    while True:
        try:
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("please enter your second number as an integer!")
        else:
            break

    #formulars

    add = (num1 + num2)
    minus = (num1 - num2)
    times = (num1 * num2)
    divide = round(num1 / num2)

    if o == "+":
        print(str(num1) + " plus " + str(num2) + " is " + str(add))
    elif o == "-":
        print(str(num1) + " less " + str(num2) + " is " + str(minus))
    elif o == "*":
        print(str(num1) + " x " + str(num2) + " is " + str(times))
    elif o == "/":
        print(str(num1) + " divide " + str(num2) + " is " + str(divide))
    else:
        print("")

calculator_1()


open("exception code.py", "r+")
