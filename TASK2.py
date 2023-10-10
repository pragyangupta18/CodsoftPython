{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def add(x, y):\
    return x + y\
\
def subtract(x, y):\
    return x - y\
\
def multiply(x, y):\
    return x * y\
\
def divide(x, y):\
    if y == 0:\
        return "Error: Division by zero"\
    return x / y\
\
while True:\
    print("Options:")\
    print("Enter 'add' for addition")\
    print("Enter 'subtract' for subtraction")\
    print("Enter 'multiply' for multiplication")\
    print("Enter 'divide' for division")\
    print("Enter 'exit' to end the program")\
\
    choice = input("Enter operation: ")\
\
    if choice == "exit":\
        print("Exiting the calculator program.")\
        break\
\
    if choice not in ["add", "subtract", "multiply", "divide"]:\
        print("Invalid choice. Please enter a valid operation.")\
        continue\
\
    try:\
        num1 = float(input("Enter first number: "))\
        num2 = float(input("Enter second number: "))\
\
        if choice == "add":\
            result = add(num1, num2)\
        elif choice == "subtract":\
            result = subtract(num1, num2)\
        elif choice == "multiply":\
            result = multiply(num1, num2)\
        elif choice == "divide":\
            result = divide(num1, num2)\
\
        print(f"Result: \{result\}")\
    except ValueError:\
        print("Invalid input. Please enter valid numbers.")\
    except Exception as e:\
        print(f"An error occurred: \{e\}")\
}