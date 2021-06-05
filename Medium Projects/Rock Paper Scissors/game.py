import random


class Game:
    computer_choice = ''
    user_choice = ''

    def __init__(self):
        self.user_name = input('Enter your name: ')
        self.rating = 0
        self.options = ''
        self.choice_dict = {}
        self.ratings_and_options(self.user_name)

    def ratings_and_options(self, name):
        print(f'Hello, {name}')
        with open('rating.txt', 'r') as f:
            while True:
                temp, rating = f.readline().split()
                if temp == name:
                    self.rating = int(rating)
                    break
        self.options = input().split(',')
        if self.options == ['']:
            self.options = ['rock', 'paper', 'scissors']
        print("Okay, let's start")
        self.user()

    def user(self):
        self.user_choice = input()
        if self.user_choice == '!exit':
            self.exit()
        elif self.user_choice in self.options:
            self.game()
        elif self.user_choice == '!rating':
            print(f'Your rating: {self.rating}')
            self.user()
        else:
            print('Invalid input')
            self.user()

    def game(self):
        index = self.options.index(self.user_choice)
        new_choices = self.options[index + 1:] + self.options[:index]
        half = len(new_choices) // 2
        winners = new_choices[:half]
        losers = new_choices[half:]
        self.computer_choice = random.choice(self.options)
        if self.user_choice == self.computer_choice:
            print(f'There is a draw {self.user_choice}')
            self.rating = self.rating + 50
        elif self.computer_choice in losers:
            print(f'Well done. The computer chose {self.computer_choice} and failed')
            self.rating = self.rating + 100
        elif self.computer_choice in winners:
            print(f'Sorry, but the computer chose {self.computer_choice}')
        self.user()

    def exit(self):
        pass


game = Game()
