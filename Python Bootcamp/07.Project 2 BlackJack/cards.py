import fun_cards as fc
# https://dev.to/nexttech/build-a-blackjack-command-line-game-3o4b


class Deck:
    '''
    Base Class
    '''

    def __init__(self, deck):
        self.deck = deck

    def __str__(self):
        pass

    def shuffle_deck(self):
        '''return a list with shuffled keys'''
        from random import shuffle
        self.shuffled_keys = list(self.deck.keys())
        shuffle(self.shuffled_keys)

    def draw_card(self):
        drawed = self.shuffled_keys[0]
        del self.shuffled_keys[0]
        return drawed


class Player():
    '''
    Player Hand
    '''

    def __init__(self):
        self.playerdeck = []
        self.playervalues = 0
        self.playeraces = 0

    def __str__(self):
        print('Playerhand:')
        for i in self.playerdeck:
            print(i)

    def add_card(self, card):
        self.playerdeck.append(card)
        # self.playervalue +=


class Dealer():
    '''
    Dealer Hand
    '''

    def __init__(self):
        self.dealerdeck = []

    def __str__(self):
        print('Dealerhand:')
        print('Hidden Card')
        for i in range(1, len(self.dealerdeck)):
            print(self.dealerdeck[i])


# Playing the game
while True:
    # rdy = ''
    # while rdy not in ["r", "rdy"]:
    #     rdy = input("Do you want to play?").lower()

    # Create a Deck of 52 Cards
    deck1 = Deck(fc.create_deck())

    # Shuffle the deck
    deck1.shuffle_deck()
    # print(deck1.shuffled_keys)

    # Create PlayerHand
    p = Player()
    # Draw a card
    p.playerdeck.append(deck1.draw_card())
    p.playerdeck.append(deck1.draw_card())
    # print(deck1.shuffled_keys)
    p.__str__()

    # Create DealerHand
    print('\n')
    d = Dealer()
    d.dealerdeck.append(deck1.draw_card())
    d.dealerdeck.append(deck1.draw_card())
    d.__str__()

    p.playerdeck.append(fc.hit_stay(deck1))
    break
