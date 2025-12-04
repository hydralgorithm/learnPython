# CALCULATOR
operator = input("Enter the operator (+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator=="+":
    print(f"{num1} + {num2} = {num1+num2}")
elif operator=="-":
    print(f"{num1} - {num2} = {num1-num2}")
elif operator=="*":
    print(f"{num1} X {num2} = {round(num1*num2,2)}")
elif operator=="/":
    if num2 == 0:
        print("Not divisible!")
    else:
        print(f"{num1} / {num2} = {round(num1/num2,2)}")
else:
    print("Invalid operator!")