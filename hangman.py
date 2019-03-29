from __future__ import print_function
import random
import time
def printHangman(x):
    if(x == 0):
        zero()
    elif(x == 1):
        one()
    elif(x == 2):
        two()
    elif(x == 3):
        three()
    elif(x == 4):
        four()
    elif(x == 5):
        five()
    elif(x == 6):
        six()
    elif(x == 7):
        seven()
def zero():
    print('  __')
    print(' |  |')
    print(' |')
    print(' |')
    print(' |')
    print(' |')
    print('_|_')
def one():
    print('  __')
    print(' |  |')
    print(' |  O')
    print(' |')
    print(' |')
    print(' |')
    print('_|_')
def two():
    print('  __')
    print(' |  |')
    print(' |  O')
    print(' |  |')
    print(' |')
    print(' |')
    print('_|_')
def three():
    print('  __  ')
    print(' |  | ')
    print(' |  O ')
    print(' | \\|')
    print(' |')
    print(' |')
    print('_|_   ')
def four():
    print('  __  ')
    print(' |  | ')
    print(' |  O ')
    print(' | \\|/')
    print(' |')
    print(' |')
    print('_|_   ')
def five():
    print('  __  ')
    print(' |  | ')
    print(' |  O ')
    print(' | \\|/')
    print(' |  | ')
    print(' |')
    print('_|_   ')
def six():
    print('  __  ')
    print(' |  | ')
    print(' |  O ')
    print(' | \\|/')
    print(' |  | ')
    print(' | /')
    print('_|_   ')
def seven():
    print('  __  ')
    print(' |  | ')
    print(' |  O ')
    print(' | \\|/')
    print(' |  | ')
    print(' | / \\')
    print('_|_   ')
print('Let\'s play hangman!')
time.sleep(1)
print('Let me think of a word hmmmmm.....')
file_words = open('lessthan20k.txt','r')
wordpkr = random.randint(0,13326)
for x in range(0,wordpkr):
    file_words.readline()
word = file_words.readline()
file_words.close()
word = word[0:len(word)-1]
time.sleep(2)
print('Got one!')
missed = 0
notword = '_'
for x in range(1,len(word)):
    notword = notword + ' _'
already_guessed = []
print(word)
#print(notword)
while(('_' in notword) and (missed < 7)):
    print('\n\n')
    printHangman(missed)
    print('Letters used:')
    print(*already_guessed, sep=' ')
    print('Guess a letter.')
    letter = raw_input(notword + '\n')
    if letter in already_guessed:
        print("You already guessed that letter!")
    elif letter in word:
        already_guessed.append(letter)
        for x in range(0,len(word)):
            if(letter == word[x]):
                notword = notword[:2*x] + letter + notword[2*x+1:]
    else:
        already_guessed.append(letter)
        print('Word does not contain {}'.format(letter))
        missed += 1
if(missed == 7):
    printHangman(missed)
    print('You lose\nHe dead')
    print('The word was {}'.format(word))
else:
    while(True):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('  O ')
        print(' \\|/')
        print('  | ')
        print(' / \\')
        print('The word was {}'.format(word))
        print('You got it! Nice work!')
        time.sleep(0.75)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('  O ')
        print('--|--')
        print('  | ')
        print(' / \\')
        print('The word was {}'.format(word))
        print('You got it! Nice work!')
        time.sleep(0.75)
