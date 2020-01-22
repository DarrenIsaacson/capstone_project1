from cardgamesetup import *

"""
Creator = Darren Isaacson
Contributor = Jordan Gerdin

This is my BlackJack Simulation Game!

Here are the rules of blackjack:

- The goal of blackjack is to beat the dealer's hand without going over 21.
- Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
- Each player starts with two cards, one of the dealer's cards is hidden until the end.
- To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
- If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
- If you are dealt 21 from the start (Ace & 10), you got a blackjack.
- Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.
- Dealer will hit until his/her cards total 17 or higher.


"""

# Main Controller of the game
def game():
    # Introduction to game
    print("Welcome to Blackjack made in Python!\n\n")

    # An instantiationi 
    computer = Player("Dealer")
    player = Player(input("Please Enter your name:"))

    player_wins = 0
    computer_wins = 0

    while(True):
        clear_all_list(player, computer)
        deck = Deck()
        deck.shuffle()
        computer,player, deck = deal_cards(computer, player, deck)

        starting_total = check_value(player)
        player_show_hand(player, starting_total)


        while(True):
            keep_going = optionselect(player, deck)
            player_total = check_value(player)
            player_show_hand(player, player_total)

            if(player_total > 21):
                break
            if(keep_going == False):
                break
            if(player_total == 21):
                break

        computer_show_hidden_hand(computer)

        while(True):
            computer_total = check_value(computer)

            if(player_total > 21):
                print("\nThe dealer reveals his hand:\n-----------------------")
                computer.showHand()
                break


            if(computer_total < 15):
                computer_draw(computer, deck)
                computer_show_hidden_hand(computer)
            elif(computer_total < player_total):
                computer_draw(computer, deck)
                computer_show_hidden_hand(computer)
            else:
                print("\nThe dealer reveals his hand:\n-----------------------")
                computer.showHand()
                break


        if(player_total > 21):
            print("You Bust!\nDealer wins!\n")
            computer_wins += 1
        elif(computer_total > 21):
            print("Dealer Bust!\nYou win!\n")
            player_wins += 1
        elif(computer_total == 21 and player_total == 21):
            print("Dealer wins with:", computer_total, "\n")
            computer_wins += 1
        elif(computer_total == 21):
            print("Dealer wins with:", computer_total, "\n")
            computer_wins += 1
        elif(computer_total > player_total):
            print("Dealer wins with:", computer_total, "\n")
            computer_wins += 1
        elif(computer_total == player_total):
            print("Dealer wins with:", computer_total, "\n")
            computer_wins += 1
        else:
            player_wins +=1
            print("You win with:", player_total)
            print("The computer had:", computer_total, "\n")

        print("Scoreboard\n-----------------------\nDealer: ", computer_wins, "\n" + player.name,": ", player_wins)
        play_again = input("\nPress enter again if you want to play again, otherwise type \"exit\" to quit\nEnter Here:")
        play_again = play_again.lower()
        if(play_again == "exit"):
            break

    print("\nThank you for playing!")

# Fucntion where cards are dealt, both to the player and computer
def deal_cards(computer,player, deck):
    print("\nYour dealer dealt 2 cards from the deck into your hand")
    player.draw(deck).draw(deck)
    computer.draw(deck).draw(deck)

    return computer,player, deck

# Function where the player must choose if they want to Hit or Stand
def optionselect(player,deck):

    print("\nDo you want to hit or stand?\nEnter 1 for hit\nEnter 2 for stand\n")

    while(True):
        try:
            hit_or_stand = int(input("Enter your option here:"))
        except ValueError:
            print("Error: Please only enter numbers 1 or 2")
            continue

        if(hit_or_stand < 1):
            print("Error: Please only enter numbers 1 or 2")
            continue
        elif(hit_or_stand > 2):
            print("Error: Please only enter numbers 1 or 2")
            continue
        else:
            break

    if(hit_or_stand == 1):
        print("\nThe dealer gave you a card\n")
        player.draw(deck)

    if(hit_or_stand == 2):
        print("\nYou have decided to stand\n")
        keep_going = False
        return keep_going

# Function to check the player and computers hand
def check_value(player):
    total = 0
    for card in player.hand:
        if(card.value < 14 and card.value > 10):
            total += 10
        elif(card.value == 14):
            if(total < 10):
                total += 11
            else:
                total += 1
        else:
            total += card.value
    return total

# Function to show the players hand and total of cards
def player_show_hand(player, total):
    print("\nYour current hand is:\n-----------------------")
    player.showHand()
    print("\nYour total is :", total, "\n")

# Function for the dealer to draw cards
def computer_draw(computer,deck):
    computer.draw(deck)

# Function for the computer to reveal his hand except 1 card
def computer_show_hidden_hand(computer):
    print("\nThe dealer hand is:\n-----------------------")
    print("{} of {}".format("????", "????"))
    for card in computer.hand[1:]:
        card.show()

# Function to clear all player and computer list for next game
def clear_all_list(player, computer):
    player.hand.clear()
    computer.hand.clear()

# initialization of the game controller.
if __name__ == '__main__':
    game()
