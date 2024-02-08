logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''




import os

os.system("cls" if os.name == "nt" else "clear")

print(logo)

bids = {}
bidding_finish = False

def find_highest(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}. ")
while not bidding_finish :
    name = input("What is your name?")
    price = int(input("What is your bid? $"))
    bids[name] = price  
    should_continue =  input("Are there any other bbidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finish = True
        find_highest(bids)
    elif should_continue == "yes":
        os.system("cls" if os.name == "nt" else "clear")



    

