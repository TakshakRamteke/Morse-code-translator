import code_dictionary              #importing the dictionary containing all the morse codes

trial_code = input("Enter your morse code : ")

letters = trial_code.split(' ')     #Spliting the morse code into individual letters

codes = code_dictionary.codes

for letter in letters : 
    for key, value in codes.items() :
        if letter == key :
            print(value,end=" ")
