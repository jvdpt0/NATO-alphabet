import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row['letter']:row['code'] for (index,row) in data.iterrows()}

success = False

while success == False:

    try:
        word = input('Enter a word: ').upper()
        nato_word = [nato_dict[letter] for letter in word]
        print (nato_word)
        success = True
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        

