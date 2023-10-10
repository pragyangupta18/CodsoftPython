{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
import string\
\
def generate_password(length):\
    # Define the character set for generating passwords\
    characters = string.ascii_letters + string.digits + string.punctuation\
\
    # Generate a random password with the specified length\
    password = ''.join(random.choice(characters) for _ in range(length))\
\
    return password\
\
def main():\
    print("Password Generator")\
    try:\
        length = int(input("Enter the desired password length: "))\
        if length <= 0:\
            print("Password length must be greater than 0.")\
        else:\
            password = generate_password(length)\
            print(f"Generated Password: \{password\}")\
    except ValueError:\
        print("Invalid input. Please enter a valid number for the password length.")\
\
if __name__ == "__main__":\
    main()\
}