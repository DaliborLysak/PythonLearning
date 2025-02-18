'''
War card game - Card
'''

from random import shuffle
import card

class Deck():
    '''
    Deck
    '''
    def __init__(self):
        # all cards
        self.cards = []
        new_cards = set()
        for suit in card.suits:
            for rank in card.ranks:
                new_cards.add(card.Card(suit=suit, rank=rank))
        self.cards = list(new_cards)

    def shuffle_deck(self):
        '''
        shufel cards
        '''
        shuffle(self.cards)

    def deal_cards(self):
        '''
        deal cards
        '''
        result = []
        for _ in range(26):
            result.append(self.cards.pop())
        return result
