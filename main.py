import pandas

# Creating a dictionary in using dictionary comprehensionn:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of nato phonetic words using list comprehension.
word = input("What is the word?").upper()
code_list = []
[code_list.append(nato_dict[letter]) for letter in word if letter in nato_dict.keys()]
print(code_list)

