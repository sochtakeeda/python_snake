"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
NTRIALS = 100    # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
    

def mc_trial(board, player):
    """
    plays a complete game with each call by alternating b/w players
    """
    
    while board.check_win() == None:
        
        # make a list of current empty squares in the grid
        empty_squares = board.get_empty_squares()
        
        # select a random empty square and make a move
        random_move = random.choice(empty_squares)
        board.move(random_move[0], random_move[1], player)
        
        # switch player
        provided.switch_player(player)
        
def mc_update_scores(scores, board, player):
    """
    updates the scores for all the squares in the grid
    """
    
    winner = board.check_win()
    if winner == provided.DRAW:
        return
    
    dimension = board.get_dim()
    for dummy_row in range(dimension):
        for dummy_col in range(dimension):
            get_square = board.square(dummy_row, dummy_col)
            
            if get_square == provided.EMPTY:
                continue
            
            if winner == player:
                if get_square == player:
                    scores[dummy_row][dummy_col] += MCMATCH
                else:
                    scores[dummy_row][dummy_col] -= MCOTHER
            else:
                if get_square == player:
                    scores[dummy_row][dummy_col] -= MCMATCH
                else:
                    scores[dummy_row][dummy_col] += MCOTHER
                    
def get_best_move(board, scores):
    """
    calculates the best move for the machine player from the updated scores and returns it
    """
    
    empty_squares = board.get_empty_squares()
    if len(empty_squares) == 0:
        return
    best_move = None
    high_score = None
    for dummy_square in empty_squares:
        if best_move == None or scores[dummy_square[0]][dummy_square[1]] > high_score:
            best_move = dummy_square
            high_score = scores[dummy_square[0]][dummy_square[1]]
    return best_move

def mc_move(board, player, trials):
    """
    calls the helper functions to score grid, calculate best move and finally makes the move
    """
    
    scores = [[0 for dummy_row in range(board.get_dim())] 
              for dummy_col in range(board.get_dim())]
    for dummy_trial in range(trials):
        board_clone = board.clone()
        mc_trial(board_clone, player)
        mc_update_scores(scores, board_clone, player)
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
