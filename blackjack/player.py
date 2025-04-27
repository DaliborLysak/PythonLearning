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

    def add_card(self, cards):
        '''
        add card to hand
        '''
        self.hand.append(cards)

    def hand_log(self):
        '''
        writes number of cards
        '''
        count = len(self.hand)
        return f"{self.name} has {count} cards"
