import random

print('-----------------')
print('  Learn to Code')
print('-----------------')
print()

# the_number = random.randint(0, 100)
the_number = random.randint(0, 100)
name = input('What is your name? ')
guess_num = -1
while guess_num != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess_num = int(guess_text)

    if guess_num < the_number:
        # print('Your guess of ' + guess_num + ' was too low')
        print('Sorry {1}, Your guess of {0} was too low'.format(guess_num, name))
    elif guess_num > the_number:
        print('Sorry {1}, Your guess of {0} was too high'.format(guess_num, name))
    else:
        print('You Win!')

print('Done')
