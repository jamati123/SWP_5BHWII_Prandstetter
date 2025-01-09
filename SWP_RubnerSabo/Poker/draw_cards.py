import random
import set_deck


deck = set_deck.main

def draw_cards(deck):
    cards_drawn = random.choice(deck)
    deck.remove(cards_drawn)
    return cards_drawn


def main():
    draw_cards(deck)


if __name__ == "__main__":
    main()