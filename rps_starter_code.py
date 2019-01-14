#!/usr/bin/env python3

import os
from random import *


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
QUESTION = "Please enter your choice - Rock Paper Scissors => "
QUESTION_VALIDATE = "Please enter valid choice - Rock Paper Scissors => "

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.their_move = None
        self.my_move_index = -1
        self.my_move = None
        self.name = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move_index = moves.index(my_move)
        self.my_move = my_move


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Random Player"

    def move(self):
        return moves[randint(1, 2)]


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Reflect Player"

    def move(self):
        if self.their_move:
            return self.their_move
        return moves[randint(1, 2)]


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Cycle Player"

    def move(self):
        if self.my_move_index > 1:
            self.my_move_index = 0
        else:
            self.my_move_index += 1
        return moves[self.my_move_index]


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Human Player"

    def move(self):
        print(f"{self.name} Turn: \n")
        valid_user_choice = False
        user_choice = input(QUESTION)

        if user_choice.strip() and user_choice.lower() in moves:
            valid_user_choice = True

        while not user_choice.strip() or not valid_user_choice:
            user_choice = input(QUESTION_VALIDATE)
            if user_choice.strip() and user_choice.lower() in moves:
                valid_user_choice = True

        return user_choice.lower().strip()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round = 0

    def check_moves(self, move1, move2):
        if move1 != move2:
            if beats(move1, move2):
                self.p1.score += 1
            else:
                self.p2.score += 1

    def display_results(self):
        clear()
        result_move = "{} move: {} - {} move: {} \n".format(
            self.p1.name,
            self.p1.my_move,
            self.p2.name,
            self.p2.my_move
            )
        print(result_move) 
        result = "{} {} - {} {} \n".format(
            self.p1.name,
            self.p1.score,
            self.p2.score,
            self.p2.name
            )
        print("======== " * 5 + "\n")
        print(result)
        print("======== " * 5 + "\n")

    def announce_winner(self):
        if self.p1.score == self.p2.score:
            print("No Winner")
        elif self.p1.score > self.p2.score:
            print(f"Winner: {self.p1.name}")
        else:
            print(f"Winner: {self.p2.name}")
        print("\n")

    def play_round(self):
        self.round += 1
        print(f"Round {self.round}: \n")
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.check_moves(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.display_results()

    def play_game(self):
        clear()
        print("Game start!")
        print("======== " * 5 + "\n")
        for round in range(3):
            self.play_round()
        self.announce_winner()
