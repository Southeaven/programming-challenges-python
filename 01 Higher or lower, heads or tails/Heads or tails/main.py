from random import randint

if __name__ == '__main__':
    while True:
        target = 'heads' if randint(0, 1) else 'tails'
        guess = input('Heads(h) or tails(t)?\n')
        if guess == 'heads' or guess == 'Heads' or guess == 'h' or guess == 'H':
            guess = 'heads'
        elif guess == 'tails' or guess == 'Tails' or guess == 't' or guess == 'T':
            guess = 'tails'
        else:
            print('Wrong input, try again!')
            continue
        if guess == target:
            print('You got it right!')
            break
        else:
            print("You are not lucky enough. Try again!")