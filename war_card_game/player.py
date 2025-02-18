'''
War card game - Player
'''

class Player():
    '''
    Player
    '''
    def __init__(self, name: str):
        self.hand = []
        self.name = name
        self.war_stack = []

    def __str__(self):
        return f"Player {self.name} has {len(self.hand)}"

    def add_cards(self, cards):
        '''
        add card to hand
        '''
        if isinstance(cards, type([])):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)

    def play_card(self):
        '''
        play top deck card
        '''
        return self.hand.pop(0)

    def hand_log(self):
        '''
        writes number of cards
        '''
        count = len(self.hand)
        return f"{self.name} has {count} cards"

    def add_card_to_war_stack(self, card):
        '''
        add card to war stack during battle of same cards
        '''
        self.war_stack.append(card)
