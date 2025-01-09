colours = ['Kreuz', 'Pik', 'Herz', 'Karo']
card_types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']


def set_deck():
    return [(colour, cardtype) for colour in colours for cardtype in card_types]

def main():
    set_deck

if __name__ == "__main__":
    main()