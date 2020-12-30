# import cards as cd
# Functions for Blackjack


def create_deck():
    # Keys for Deck-Dictionary
    cardtype = ['Clubs ', 'Diamonds ', 'Hearts ', 'Spades ']
    cardface = ['Ace', '2', '3', '4', '5', '6',
                '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    # Values for Deck-Dictionary
    cardvalue = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

    keys = [x + y for x in cardtype for y in cardface]
    deck = dict(zip(keys, cardvalue))
    return deck


def check_ace_value():
    '''Check if Ace should be 1 or 10'''
    pass


def hit_stay(deck):
    '''Ask the Player: Hit or Stay'''
    choice = ''
    while choice not in ['hit', 'h', 'stay', 's']:
        choice = input('Hit or Stay? ').lower()
    if choice in ['hit', 'h']:
        print("You have choosen to Hit: Card Draw")
        return deck.draw_card()

    else:
        print("You have choosen to Stay: Nothing")
