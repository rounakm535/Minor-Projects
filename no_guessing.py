logo = '''
   ___                       _   _                __                 _               
  / _ \_   _  ___  ___ ___  | |_| |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \__|_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                     

'''

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def game():
    
    print(logo)

    print("Welcome to the Number Guessing Game.")
    print("I,m thinking a number between 1 and 100.")


    def check_answer(guess, answer, turns):
        if guess > answer:
            print(f"Too high...")
            return turns - 1
        elif guess < answer:
            print(f"Too low...")
            return turns - 1
        elif guess == answer:
            print(f"Yoohooo! You got it. The answer was {answer}")
        else :
            print("Write a valid input...")

    def set_diff():
        level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
        if level == "easy" :
            return EASY_LEVEL_TURNS
        else :
            return HARD_LEVEL_TURNS
        

    answer = randint(1, 100)
    # print(f"The no. is {answer}")

    turns = set_diff()


    guess = 0

    while guess != answer:

        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))    

        turns = check_answer(guess, answer, turns)
        
        if turns == 0 :
            print("You have ran out of guesses. :(")
            print(f"The number was {answer}")
            return
        

game()
