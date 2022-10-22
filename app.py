from curses.ascii import isdigit
from random import randint
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favourite_animal(users_animal):
    """Display a message to the user that changes based on their favourite animal"""
    return f'Wow, {users_animal} is my favourite animal too!'

@app.route('/dessert/<users_dessert>')
def favourite_dessert(users_dessert):
    """Display a message to the user that changes based on their favourite dessert"""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def story(adjective, noun):
    """Display a story to the user that changes based on the adjective and noun they supply"""
    return f'The {noun} got in their {adjective} car and drove to town.  The end.'

@app.route('/multiply/<number1>/<number2>')
def multiplication(number1, number2):
    """Display a multiplication statement with its product based on two numbers supplied by the user"""
    # Check if all characters in the supplied arguments are digits
    number1_num_digits = 0
    for character in number1:
        if isdigit(character):
            number1_num_digits+= 1
    
    number2_num_digits = 0
    for character in number2:
        if isdigit(character):
            number2_num_digits+= 1
    
    if number1_num_digits == len(number1) and number2_num_digits == len(number2):
        return f'{number1} times {number2} is {int(number1) * int(number2)}'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    """Display a string (provided by the user) a number(provided by the user) of times, each string separated by a space"""
    number_of_digits_in_n = 0
    for character in n:
        if isdigit(character):
            number_of_digits_in_n+= 1

    if number_of_digits_in_n == len(n):
        output_string = ''
        for i in range(int(n)):
            output_string = output_string + word + ' '
        return f'{output_string}'
    else:
        return 'Invalid input. Please try again by entering a word and a number!'

@app.route('/dicegame')
def roll_dice():
    """Display a random integer between 1 and 6, inclusive"""
    result = randint(1, 6)
    if result == 6:
        return f'You rolled a {result}.  You won!'
    else:
        return f'You rolled a {result}. You lost!'

if __name__== '__main__':
    app.run(debug=True)

