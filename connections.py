import json
import random


class Connections:

    def __init__(self, path):
        self.load_puzzle(path)
        self.get_terms()
        
        self.tries_remaining = 4
        self.solved = False
        self.solved_terms = []

    def load_puzzle(self, path):
        with open(path, 'r') as f:
            self.puzzle = json.load(f)
        
    def get_terms(self):
        self.terms = []

        for k, v in self.puzzle.items():
            self.terms += v

        random.shuffle(self.terms)

    def show_title_screen(self):
        print('*****************************************************************')
        print('*                          CONNECTIONS                          *')
        print('*                      Make groups of four                      *')
        print('*****************************************************************')
        print()
        
    def display_board(self):
        for i, term in enumerate(self.terms, 1):
            t = term.upper()
            print(f'{t:16}', end='')

            if i % 4 == 0:
                print()
        print()
        print(f'Guesses left: {self.tries_remaining}')
        print()

    def get_guess(self):
        print('Pick 4 (separate your terms with commas)')
        guess = input('>')

        guess_list = guess.split(',')
        guess_list = [term.strip() for term in guess_list]
                      
        return guess_list

    def check_guess(self, guess):
        sorted_guess = sorted(guess)
        
        for category, terms in self.puzzle.items():
            sorted_terms = sorted(terms)

            if sorted_guess == sorted_terms:
                print(category)
                return True
                
        print('Nope.')
        
        return False

    def show_result(self):
        if self.solved:
            print('Great job!')
        else:
            print('You lose.')
            
    def play(self):
        self.show_title_screen()
        
        while not self.solved and self.tries_remaining > 0:
            self.display_board()

            guess = self.get_guess()
            correct = self.check_guess(guess)

            if correct:
                self.solved_terms += guess

                for t in guess:
                    self.terms.remove(t)
            else:
                self.tries_remaining -= 1

            if len(self.solved_terms) == 16:
                self.solved = True
                
        self.show_result()
        

# Let's do this!
if __name__ == '__main__':
    g = Connections('puzzles/2023-11-10.json')
    g.play()


