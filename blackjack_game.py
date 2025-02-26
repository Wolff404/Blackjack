import blackjack_module as bjm

def deal_cards():
    for i in range(2):
        players_hand.append(shuffled_deck.pop())
        dealers_hand.append(shuffled_deck.pop())

def print_hand(cards):
    string = "a "
    for index, card in enumerate(cards): #bruker enumerate for å ta i mot listen og ønsker å returnerer liste elementene og posisjonene.
        string += card
        if index < len(cards) - 1:
            if index == len(cards)-2:
                string += " and a "
            else:
                string += " , "
    return string


def print_results(players_cards, dealers_cards):
    global prize
    player_score = bjm.calculate_hand_value(players_cards)
    dealer_score = bjm.calculate_hand_value(dealers_cards)
    if dealer_score > 21:
        print(f"Dealer busted, you win! You currently have {chips}")
        prize = players_bet

    elif player_score > dealer_score:
        print("You beat the dealer, you win!")
        prize += players_bet

    elif dealer_score > player_score:
        print("The dealer has a higher value at hand, you lose...")
        prize -= players_bet

    elif dealer_score == player_score:
        print("You have the same score as the dealer. No one wins.")

chips = 5
prize = 0

while True:
    shuffled_deck = bjm.get_new_shuffled_deck()
    players_hand = []
    dealers_hand = []
    prize = 0
    players_bet = None

    while not players_bet:
        try:
            print(f"You currently have: {chips} chips \n")
            players_bet = int(input("How many chips do you want to bet?"))
            print(f"Your bet is with: {players_bet} chips \n")
        except ValueError:
            print("You must enter a number (for example: 5 )")
        else:
            if players_bet > chips:
                players_bet = None
                print("You cant bet more chips than you already have \n")

    deal_cards()
    print(f"The cards have been dealt. You have a {print_hand(players_hand)}, "
          f"with a total of {bjm.calculate_hand_value(players_hand)}\n")
    print(f"The dealers visable card is {dealers_hand[0]}, with a value of {bjm.calculate_hand_value(dealers_hand)}\n")

    if bjm.calculate_hand_value(players_hand) == 21:
        print("You have a blackjack, you win!")
        prize = players_bet * 2
        #break, ønsket at den kunne breaket her for å restarte spillet, men ble kluss med hele loopen. altså den andre while loopen ville fortsette og gi ut kort.

    # if bjm.calculate_hand_value(dealers_hand) == 21:
    #    print("Dealer has a blackjack, you lost.")

    else:
        while True:
            action = input("Would you like to hit or stand?")
            print()
            while action not in ("stand", "hit"):
                action = input("Invalid choice, try again:")

            if action == "hit":
                players_hand.append(shuffled_deck.pop())
                print(f"Your cards are currently {print_hand(players_hand)} with the value of {bjm.calculate_hand_value(players_hand)} \n")
                if bjm.calculate_hand_value(players_hand) > 21:
                    print("You busted. you lose.")
                    prize -= players_bet
                    break

            elif action == "stand":
                print(f"You chose to stand.\n")
                while bjm.calculate_hand_value(dealers_hand) < 18:
                    dealers_hand.append(shuffled_deck.pop())
                    print("Dealer draws a card")
                    print(f"The dealers cards are {print_hand(dealers_hand)} "
                      f"with a value of {bjm.calculate_hand_value(dealers_hand)}\n")
                print(f"Your cards are {print_hand(players_hand)}, with a value of {bjm.calculate_hand_value(players_hand)}\n")
                print_results(players_hand, dealers_hand)
                break

    chips += prize
    if prize > 0:
        print(f"You won {abs(prize)} chips, your new total is {chips} chips.") #bruker (abs) for å få en absolutt verdi på printen. Uten (abs) vil printen komme ut som du mistet -5 chips istedenfor du mistet 5 chips. (Dobbel negativ?)
    elif prize < 0:
        print(f"You lost {abs(prize)} chips, your new total is {chips} chips.")
    else:
        print(f"Its a tie, your bet has been returned. You still have {chips} chips")

    if chips <= 0:
        print("You cant play anymore, because you have no chips")
        exit()
    play_again = input("\nDo you want to play again? y/n: ")
    if play_again != "y":
        break