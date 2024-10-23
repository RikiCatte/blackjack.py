import random

suits = ['hearts', 'spades', 'clubs', 'diamonds']  # cuori, picche, fiori, quadri

def create_deck():
    deck = {}
    
    for suit in suits:
        for rank in range(1, 14):
            if rank == 1:
                val = 'A'
            elif rank == 11:
                val = 'J'
            elif rank == 12:
                val = 'Q'
            elif rank == 13:
                val = 'K'
            else:
                val = str(rank)
                
            key = f"{val} of {suit}"
            deck[key] = rank if rank <= 10 else 10
    return deck

def shuffle_deck(deck):
    deck_items = list(deck.items())
    random.shuffle(deck_items)
    deck = dict(deck_items)
    return deck

def draw(deck):
    if len(deck) > 0:
        first_element_key = next(iter(deck))  # Gets the key of dict's first element
        return (first_element_key, deck.pop(first_element_key))
    else:
        return None, "Deck is empty"

def return_score(hand):
    score = 0
    for card in hand:
        score += card[1]  # Since the hand now stores tuples, we use card[1] to get the score
    return score

def player(deck):
    hand = []
    card = draw(deck)
    if card[0] is not None:  # Check if the deck is not empty
        hand.append(card)
    done = False

    while (return_score(hand) < 21) and not done:
        choice = ""
        while choice != "Y" and choice != "N":
            print(f"Hand: {', '.join([c[0] for c in hand])} - Total Score: {return_score(hand)}")
            choice = input("Do you want to draw again? Y/N ")
        if choice == "Y":
            card = draw(deck)
            if card[0] is not None:
                hand.append(card)
        else:
            done = True
    print("Player's final hand: ", ', '.join([c[0] for c in hand]))
    return hand

def dealer(deck, player_score):
    hand = []
    card = draw(deck)
    if card[0] is not None:
        hand.append(card)
    while return_score(hand) < 21 and (return_score(hand) < player_score):
        print("Dealer's hand: ", ', '.join([c[0] for c in hand]))
        card = draw(deck)
        if card[0] is not None:
            hand.append(card)
    print("Dealer's final hand: ", ', '.join([c[0] for c in hand]))
    print("Dealer's final score: ", return_score(hand))
    return hand      

def play():
    deck = shuffle_deck(create_deck())
    player_hand = player(deck)
    player_score = return_score(player_hand)
    print("Player's score: ", player_score) 
    if player_score > 21:
        print("You lose!")
        return
    dealer_hand = dealer(deck, player_score)
    dealer_score = return_score(dealer_hand)
    if dealer_score > 21 or dealer_score < player_score:
        print("You won!")
        return
    print("You lose!")

play()