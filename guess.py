#this program is a guessing game, you pick a number between 1 and 100 and it
#will try to guess it at random. You must give hints whether it is higher or
#lower than the computers guess. The program will output how many times it
#had to guess at the end

#Inspiration for game came from www.practicepython.org
import time
import random
print("Pick a number between 1 and 100, inclusively.")
#time.sleep(3)
print("Got it?")
#time.sleep(2)
print("I'm going to guess it! Please answer with yes, higher, or lower.")
#time.sleep(2)
hi_val=100
lo_val=1
found = False
guesses = 1
while(found == False):
    guess = random.randint(lo_val, hi_val)
    question = "Is your number " + str(guess) + "?"
    ans = raw_input(question)
    if(ans == 'yes'):
        print('Got ya!')
        print('Number of guesses = ' + str(guesses))
        break
    elif(ans == 'higher'):
        lo_val = guess+1
    elif(ans == 'lower'):
        hi_val = guess-1
    else:
        print("not a valid input")
        break
    guesses += 1
