#Name: Naidra Gardner
#   Prog Purpose: This Magic 8-ball code uses a Python tuple since the
#   user does not have the ability to change the 8-ball answers.
#   However, the program could have used a Python list instead of a tuple.
#   NOTE: Tuples uses parenthese; lists uses square braces.

import random
answers_8_ball = ("As I see it, yes", "Ask again later",
    "Better not tell you now", "Cannot predict now",
    "Concentrate and ask again", "Don't count on it",
    "It is certain", "It is decidedly so",
    "Most likely", " My reply is no",
    "My sources says no", "Outlook good",
    "Signs point to yes", " Very doubtful",
    "Without a doubt", "Yes",
    "Yes definitely", "You may rely on it",)

def main():

    print("I am the MAGIC-8 BALL and can answer any YES or NO question!")

    another_question = True
    while another_question:
        answer = random.choice(answers_8_ball)

        print("\nShake the MAGIC 9 BALL")
        print("...and now...")
        question = input("\nWhat is your YES or NO question?")
        print("The MAGIC 8 BALL says:" + answer)

        askAgain = input("\nWould you like to ask me another question (Y or N)?:" )
        if askAgain.upper() == "N" or askAgain == "n":
            another_question = False

    print("\nCome back again when you have other important questions.")
    print("...Magic-8 Ball OUT.")

main()
