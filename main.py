from rps_starter_code import *

if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
