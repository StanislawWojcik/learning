# rock, paper, scissors
from random import choice

class Game():
    def __init__(self):
        self.rps_list = ['rock', 'paper', 'scissors']
        self.counter = 0
        self.user_win = 0
        self.comp_win = 0

    def start(self):
        while self.counter < 3:
            self.comp_choice = choice(self.rps_list)
            self.user_choice = input('Please, type down your choice: ')
            if self.comp_choice == self.user_choice:
                print(f'{self.user_choice} vs. {self.comp_choice}! Draw!')
                self.counter += 1
            else:
                    if self.user_choice == 'paper':
                        if self.comp_choice == 'rock':
                            print(f'{self.user_choice} beats {self.comp_choice}! Point for you!')
                            self.user_win += 1
                            self.counter += 1
                        if self.comp_choice == 'scissors':
                            print(f'{self.user_choice} beats {self.comp_choice}! Point for computer! ')
                            self.counter += 1
                            self.comp_win += 1

                    if self.user_choice == 'rock':
                        if self.comp_choice == 'scissors':
                            print(f'{self.user_choice} beats {self.comp_choice}! Point for you!')
                            self.counter += 1
                            self.user_win += 1
                        if self.comp_choice == 'paper':
                            print(f'{self.user_choice} beats {self.comp_choice}! Point for computer')
                            self.counter += 1
                            self.comp_win += 1

                    if self.user_choice == 'scissors':
                        if self.comp_choice == 'paper':
                            print(f'{self.user_choice} beats {self.comp_choice}! Point for computer')
                            self.counter += 1
                            self.user_win += 1
                        if self.comp_choice == 'rock':
                            print(f'{self.user_choice} beats {self.comp_choice}! Point for computer')
                            self.counter += 1
                            self.comp_win += 1
    def who_win(self):

        if self.comp_win > self.user_win:
            print(f'You lost {self.comp_win} to {self.user_win}')
        if self.user_win > self.comp_win:
            print(f'You won {self.user_win} to {self.comp_win}')
        if self.comp_win == self.user_win:
            print(f'{self.user_win} to {self.comp_win}! Thats a tie!')

print('rock, paper or scissors?')
while True:
    lets_play = Game()
    lets_play.start()
    lets_play.who_win()
    odp = input('Would you like to play again? y/n ')
    if odp == 'n':
        break
    if odp == 'y':
        continue
