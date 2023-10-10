{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
\
def determine_winner(user_choice, computer_choice):\
    if user_choice == computer_choice:\
        return "It's a tie!"\
    elif (\
        (user_choice == "rock" and computer_choice == "scissors") or\
        (user_choice == "scissors" and computer_choice == "paper") or\
        (user_choice == "paper" and computer_choice == "rock")\
    ):\
        return "You win!"\
    else:\
        return "Computer wins!"\
\
def main():\
    user_score = 0\
    computer_score = 0\
\
    print("Welcome to Rock-Paper-Scissors Game!")\
\
    while True:\
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()\
\
        if user_choice == "quit":\
            break\
\
        if user_choice not in ["rock", "paper", "scissors"]:\
            print("Invalid choice. Please choose rock, paper, or scissors.")\
            continue\
\
        computer_choice = random.choice(["rock", "paper", "scissors"])\
        print(f"You chose: \{user_choice\}")\
        print(f"Computer chose: \{computer_choice\}")\
\
        result = determine_winner(user_choice, computer_choice)\
        print(result)\
\
        if result == "You win!":\
            user_score += 1\
        elif result == "Computer wins!":\
            computer_score += 1\
\
        print(f"Your score: \{user_score\}")\
        print(f"Computer's score: \{computer_score\}")\
\
if __name__ == "__main__":\
    main()\
}