#BLACKJACK
import random
import os
clear = lambda: os.system('cls')

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

end = True


def add_random_card(list):
    """append a random number into a given list"""
    card = random.choice(cards)
    list.append(card)


def sum_of_cards(list):
    """returns the sum of numbers in a list"""
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum


def game():
    clear()
    player_hand = []
    computer_hand = []
    add_random_card(player_hand)
    add_random_card(computer_hand)
    print(logo)
    print(f"Computer's first card: {computer_hand[0]}")
    end_of_game = False
  

    while end_of_game == False:
        add_random_card(player_hand)
        if 11 in player_hand and sum_of_cards(player_hand) > 21:
            player_hand.remove(11)
            player_hand.append(1)

        print(f"Your cards: {player_hand}, current score: {sum_of_cards(player_hand)}")

        if sum_of_cards(player_hand) > 21:
            end_of_game = True
            break
        answer2 = input("Type 'y' to get another card, type 'n' to pass: ")
        if answer2 == "n":
            end_of_game = True

    if sum_of_cards(computer_hand) < 17:
        add_random_card(computer_hand)
        print(f"Computer's cards: {computer_hand}")

    if sum_of_cards(player_hand) > 21:
        print(f"\nYou lose because your hand: {player_hand} is {sum_of_cards(player_hand)}\n")

    elif sum_of_cards(player_hand) > sum_of_cards(computer_hand):
        print(
            f"\nYou win with {player_hand}: {sum_of_cards(player_hand)} and computer lost with {computer_hand}: {sum_of_cards(computer_hand)}\n")
    elif sum_of_cards(player_hand) == sum_of_cards(computer_hand):
        print(
            f"\nDraw with {player_hand}: {sum_of_cards(player_hand)} and computer {computer_hand}: {sum_of_cards(computer_hand)}\n")
    else:
        print(
            f"\nYou lose with {player_hand}: {sum_of_cards(player_hand)} and computer wins with {computer_hand}: {sum_of_cards(computer_hand)}\n")


while 1 == 1:
    answer = input("Do you want to start a game? 'y' or 'n' ")
    if answer == "y":
        game()
    else:
        break
