import random
import os

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

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards):
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(userscore, dealerscore):
    if userscore == dealerscore:
        return "It's a Draw!!!"
    elif dealerscore == 0:
        return "You lose, dealer has a Blackjack!!!"
    elif userscore == 0:
        return "You win with a Blackjack!!!"
    elif userscore > 21:
        return "You went over 21, you lose!!!"
    elif dealerscore > 21:
        return "Dealer went over 21, you win!!!"
    elif userscore > dealerscore:
        return "You win!!!"
    else:
        return "You lose!!!"

def play_game():
    print(logo)
    user_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards},   current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        dealer_cards.append(deal_card())
        computer_score = calculate_score(dealer_cards)

    print(f"    Your final hand: {user_cards},  final score: {user_score}")
    print(f"    Dealer's final hand: {dealer_cards},  final score: {dealer_score}")
    print(compare(user_score, dealer_score))

while input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system('cls')
    play_game()