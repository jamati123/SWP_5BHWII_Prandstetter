import draw_cards

def draw_hand():
    return [draw_cards.main for _ in range(5)]


def main():
    hand = draw_hand
    print(hand)
    draw_hand()

if __name__ == "__main__":
    main()  