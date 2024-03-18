from art import logo
from art import vs
from game_data import data
import random
import os
os.system("cls" if os.name == "nt" else "clear")


def format_data(acc):

    acc_name = acc["name"]
    acc_desc = acc["description"]
    acc_coun = acc["country"]
    return f"{acc_name}, a {acc_desc}, from {acc_coun}"


def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else :
        return guess == "b"
    

print(logo)
score = 0
game_cont = True
acc_b = random.choice(data)


while game_cont :

    acc_a = acc_b
    acc_b = random.choice(data)
   
    while acc_a == acc_b:
        acc_b = random.choice(data)

    print(f"Compare A: {format_data(acc_a)}")
    print(vs)
    print(f"Compare B: {format_data(acc_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower = acc_a["follower_count"]
    b_follower = acc_b["follower_count"]
    is_correct = check_answer(guess, a_follower, b_follower)
    os.system("cls" if os.name == "nt" else "clear")

    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else :
        game_cont = False
        print(f"Sorry that's wrong. Final Score: {score}")
