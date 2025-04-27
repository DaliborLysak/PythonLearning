'''
 card game
'''

import deck
import player
import card

def init_game():
    '''
    init game
    '''
    game_deck = deck.Deck()
    game_deck.shuffle_deck()
    player1 = player.Player("Player")
    player1.add_card(game_deck.deal_card())
    return player1

def log(player1: player.Player):
    '''
    logs game status
    '''
    print(player1.hand_log())

def run_game():
    '''
    run game
    '''
    player1 = init_game()
    # log(player1)

run_game()
