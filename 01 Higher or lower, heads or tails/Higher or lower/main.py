from random import randint

if __name__ == '__main__':
    target = randint(1, 1000)
    print('I am thinking about a number between 1 and 1000. Try to guess it!')
    while True:
        guess = int(input())
        if guess == target:
            print('You got it! Good job!')
            break
        else:
            if guess > target:
                print('My number is smaller!')
            else:
                print('My number is bigger!')