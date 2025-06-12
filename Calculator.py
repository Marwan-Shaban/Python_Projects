print(" Calculator ")

Num1 = float(input("Please, Enter the first number : "))
process = input("Please, Enter your process :  ")
Num2 = float(input("Please, Enter the second number : "))

if process == "+":
    print(Num1 + Num2)
elif process == "-":
    print(Num1 - Num2)
elif process == "*":
    print(Num1 * Num2)
elif process == "/":
    print(Num1 / Num2)
elif process == "%":
    print(Num1 % Num2)
else:
    print("Wrong... Please try again")
