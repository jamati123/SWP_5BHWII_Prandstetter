import random
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd


colours = ['Kreuz', 'Pik', 'Herz', 'Karo']
card_types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']

combinations = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two Pair": 0,
    "One Pair": 0,
    "High Card": 0
}

how_many = 100000
handsize = 5

def set_deck():
    return [(colour, cardtype) for colour in colours for cardtype in card_types]

def draw_cards(deck):
    cards_drawn = random.choice(deck)
    deck.remove(cards_drawn)
    return cards_drawn

def draw_hand(deck):
    return [draw_cards(deck) for _ in range(handsize)]
#   return [random.choice(deck) for _ in range(handsize)]

def set_range(card):
    rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'Bube': 9, 'Dame': 10, 'König': 11, 'Ass': 12}
    return rank_order[card]

def order(hand):
    return sorted(hand, key=lambda card: set_range(card[1]))

def royal_flush(hand):
    rf = ['10', 'Bube', 'Dame', 'König', 'Ass']
    colour_in_hand = [card[0] for card in hand]
    symbol_hand = [card[1] for card in hand]
    return len(set(colour_in_hand)) == 1 and all(type in symbol_hand for type in rf)

def determine_combination(hand):
    colour_in_hand = [card[0] for card in hand]
    symbol_hand = [card[1] for card in hand]
    counter_cards = Counter(symbol_hand)
  

    
    sorted_hand = order(hand)
    sorted_values = [set_range(card[1]) for card in sorted_hand]

    if royal_flush(hand):
        return "Royal Flush"

    elif len(set(colour_in_hand)) == 1 and sorted_values == list(range(sorted_values[0], sorted_values[0] + 5)):
        return "Straight Flush"
    
    elif 4 in counter_cards.values():
        return "Four of a Kind"

    elif 2 in counter_cards.values() and 3 in counter_cards.values():
        return "Full House"

    elif len(set(colour_in_hand)) == 1:
        return "Flush"

    elif sorted_values == list(range(sorted_values[0], sorted_values[0] + 5)):
        return "Straight"

    elif 3 in counter_cards.values():
        return "Three of a Kind"

    elif list(counter_cards.values()).count(2) == 2:
        return "Two Pair"

    elif 2 in counter_cards.values():
        return "One Pair"
    
    return "High Card"


def main():
    for _ in range(how_many):
        deck = set_deck()
        hand = draw_hand(deck)
        combination = determine_combination(hand)
        combinations[combination] += 1

    for combination, amount in combinations.items():
        
        df = pd.DataFrame([[combinations]], columns=["Combination"]) 
        with pd.ExcelWriter("/home/florian/Documents/GithubRepos/SWP/SWP_5BHWII_Prandstetter/SWP_RubnerSabo/poker.xlsx") as writer:
            df.to_excel(writer)
        print(f"{combination}: {amount} ({amount/how_many*100:.9f}%)")
    
    print("Ziehungen: ", how_many)



if __name__ == "__main__":
    main()

    