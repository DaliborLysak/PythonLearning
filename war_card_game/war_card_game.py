'''
War card game
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
    player1 = player.Player("player 1")
    player1.add_cards(game_deck.deal_cards())
    player2 = player.Player("player 2")
    player2.add_cards(game_deck.deal_cards())
    return (player1, player2)

def play(player1: player.Player, player2: player.Player):
    '''
    game play algorithm
    '''
    if is_end(player1, player2):
        return # end during the war
    player1_card : card.Card = player1.play_card()
    player2_card : card.Card  = player2.play_card()
    if player1_card.value > player2_card.value:
        player1.add_cards(player1_card) # return
        player1.add_cards(player2_card)
        handle_endof_war(player1, player2)
    elif player1_card.value < player2_card.value:
        player2.add_cards(player2_card) # return
        player2.add_cards(player1_card)
        handle_endof_war(player2, player1)
    else:
        war(player1, player1_card, player2, player2_card)

def war(player1: player.Player,
        player1_card: card.Card,
        player2: player.Player,
        player2_card: card.Card):
    '''
    same card war in process
    '''
    player1.add_card_to_war_stack(player1_card)
    player2.add_card_to_war_stack(player2_card)
    play(player1, player2)

def handle_endof_war(player_winner: player.Player, player_looser: player.Player):
    '''
    handle end of war, winer takes all
    '''
    player_winner.add_cards(player_winner.war_stack) # return
    player_winner.add_cards(player_looser.war_stack)
    player_winner.war_stack = []
    player_looser.war_stack = []

def is_end(player1: player.Player, player2: player.Player):
    '''
    detects end of game
    '''
    return len(player1.hand) == 0 or len(player2.hand) == 0

def log(player1: player.Player, player2: player.Player):
    '''
    logs game status
    '''
    print(player1.hand_log())
    print(player2.hand_log())

def log_winner(player1: player.Player, player2: player.Player):
    '''
    log winner
    '''
    winner = player1 if len(player1.hand) > len(player2.hand) else player2
    print(f"Winner is {winner.name}")

def run_game():
    '''
    run game
    '''
    player1, player2 = init_game()
    # log(player1, player2)
    while not is_end(player1, player2):
        play(player1, player2)
        log(player1, player2)

    #end of game
    # log(player1, player2)
    log_winner(player1, player2)


run_game()
