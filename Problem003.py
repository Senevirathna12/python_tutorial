word = input(f"Please enter your word :")

if word.endswith('ing'):
    print(f" Removing 'ing' : {word[:-3]}")
else:
    print(f"No 'ing' ,your word is {word}")