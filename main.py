import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_data_frame = pandas.DataFrame(alphabet)

text = input("Please enter a value to be translated using the NATO alphabet:")
alphaList = []

for letter in text:
    for (index, row) in alphabet_data_frame.iterrows():
        if(letter.upper() == row.letter):
            alphaList.append(row.code)
print(alphaList)
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

