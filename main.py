
# Setting up a while loop for future use, but right now it would
# just get in the way so it's commented out.
# bidders = "y"
# while bidders == "y":
#   name = input("Please enter bidder's name: ")
#   bidAmt = input("Please enter your bid amount: $")

bidders = {
    "Jay" : 10,
    "Steve" : 35,
    "Linus" : 176,
    "Paul" : 62
}

# highBid = max(bidders, key=bidders.get)]
highBidder = ""
highBid = 0
for bidder in bidders:
    bid = bidders[bidder]
    if highBid < bid:
        highBid = bid
        highBidder = bidder
print(f"{highBidder} wins with a bid of ${highBid}!")
    