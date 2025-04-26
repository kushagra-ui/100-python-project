print("Welcome to the Auction!")
logo = '''  ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ '''
print(logo)
def find_highest_bidder(bidding_dictinary):
    winner = ""
    highest_bid=0
    for bidder  in bidding_dictinary: 
        bid_amount = bidding_dictinary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    print(f"The winner is {winner} with a bid of ${highest_bid}.  ")    

bids = {}

continue_bidding = True
while continue_bidding:
    Name = input("Enter your Name: \n ") 
    bid_price = int(input("Enter the Bid you want : \n $ "))
    bids[Name] = bid_price
    should_continue = input("are there any other bidders? type 'yes' or 'no'. \n ").lower()
    if should_continue=="no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" *20)    
   
   
   
        
             
     