trial_code = input("Enter your morse code : ")

letters = trial_code.split(' ')  ## Spliting the morse code into individual letters

codes = {
    'A':'._',
    'B':'_...',
    'C':'_._.',
    'D':'_..',
    'E':'.',
    'F':'.._.',
    'G':'__.',
    'H':'....',
    'I':'..',
    'J':'.___',
    'k':'_._',
    'L':'._..',
    'M':'__',
    'N':'_.',
    'O':'___',
    'P':'.__.',
    'Q':'__._',
    'R':'._.',
    'S':'...',
    'T':'_',
    'U':'.._',
    'V':'..._',
    'W':'.__',
    'X':'_.._',
    'Y':'_.__',
    'Z':'__..',
    
}

for letter in letters : 
    for key, value in codes.items(): 
        if letter == value :
            print(key,end=" ")
