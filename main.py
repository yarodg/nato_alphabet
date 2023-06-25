import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from dataframe
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_word = [phonetic_dict[char] for char in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_word)


generate_phonetic()
