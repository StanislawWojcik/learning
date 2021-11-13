# user has to guess the randomly chosen number
# the game helps by narrowing the range
from random import randint

class Guess_the_number():
    def __init__(self):
        self.lower_range = 1
        self.upper_range = 100

    def get_random_number(self):
        self.random_number = randint(self.lower_range, self.upper_range)
        self.user_number = 0
        return self.random_number

    def start(self):
        user_number = 0
        random_number = self.get_random_number()
        lower_range = self.lower_range
        upper_range = self.upper_range
        counter = 0
        while user_number != random_number:
            user_number = int(input('Enter the number: '))
            if user_number > random_number:
                upper_range = user_number - 1
                print('Too high!!')
                print(f'Guess the number in range from {lower_range} to {upper_range}')
                counter = counter + 1
            if user_number < random_number:
                lower_range = user_number + 1
                print('Too low!')
                print(f'Guess the number in range from  {lower_range} to {upper_range}')
                counter = counter + 1
            if user_number == random_number:
                print('You win! Congratulations!')
                print(f'It took you {counter} rounds')

print('Guess the number from range 1-100')
gra = Guess_the_number()
gra.start()
