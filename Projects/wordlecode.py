print ("guess a 5 letter word")

import random

# Pick a word at random
word_list = ["loopy","large","silly","poops","sigma","penny","class","monks","pizza","feins","shank","splat","goons","dildo"]
hidden_word = random.choice(word_list)

# repeat for 6 guesses
for i in range(6):
    guess_word = input()
    output = ""

    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟧"
    else:
        output += "⬛"
    
    
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟧"
    else:
        output += "⬛"
    
    
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟧"
    else:
        output += "⬛"
    
    
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟧"
    else:
        output += "⬛"
    
    
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟧"
    else:
        output += "⬛"
    
    # Result
    print (output)
    if output == "🟩🟩🟩🟩🟩":
        print ("you got it")
        break

print (f"you used {i+1} guesses")