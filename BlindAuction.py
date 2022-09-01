#BID BLIND AUCTION
import os

clear = lambda: os.system('cls')
players = {}
name = ""
bid = 0
winner = "eu"
end = False


def add_player(name, bid):
    """ Populate a dict with the name and bid of a player"""
    players[name] = bid


while end != True:
    name = input("Enter name: ")
    bid = input("Enter the sum: $")
    add_player(name, bid)
    option = input("Do you want to add more players? Yes or No ")
    clear()
    if option == "no":
        end = True

for player in players:
    if players[player] >= bid:
        winner = player
        bid = players[player]

print(f"The winner is {winner} with ${bid}")
