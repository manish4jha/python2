# The word jumble game

import random

# List words from which random a word is chosen
words = ['apples', 'computer', 'carbon', 'oxygen', 'laptop', 'python', 'cherries']

random.shuffle(words)
#print(words)

# print the banner
print('-'*40)
print('\tTHE WORD JUMBLE GAME')
print('-'*40)

score = 0


# Gaming loop
for word in words: # # Repeat the process for several times

    # Some logic to jumble the word
    chars  = list(word)
    random.shuffle(chars)
    jword = ''.join(chars)

    # Present the jumbled word to the user
    print('GUESS THIS WORD: ', jword)

    # Allow the user to guess the actual word and input
    uword = input('>>> ')

    # Do a comparison and keep the score
    if(uword == word):
        print('Correct guess!')
        score += 1
    else:
        print('Incorrect guess..')

    
# Finally present the report
print('-'*30)
print('SCORE : ', score)
if(score > int(0.7 * len(words))):
    print('Your playing is excellent')
else:
    print('Give a better try next time')

# Improvement tips:
# 1. Multiple lists in different levels [1 2 3 4 5]
# 2. You can ask the user from which level he wants to start
# 3. Automatically go to the next level as soon as the level is completed
# 4. By default it should always start from level one
# 5. Keep the scores in a file under different users/player
# 6. Create a facility to show the graph of performance of various players
# 7. Move the list of words into a file
# 8. Can you make this game to be played over the network?
# 9. Can there be a graphical user interface for this game?
# 10. Can there be a website/web application to play this game?

