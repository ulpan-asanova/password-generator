import random

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password                  


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
messup = 'il1Lo0O'

print("The number of required passwords:")

number = int(input())

for i in range(number):
    chars = ''
    print ("The required length of the", i+1, "password:")
    length = int(input())
    
    print("Do you want digits in your password? Yes or No")
    ifd = input()
    if ifd == 'Yes':
        chars += digits
        
    print("Do you want lowercase letters in your password? Yes or No")
    ifl = input()
    if ifl == 'Yes':
        chars += lowercase_letters
        
    print("Do you want uppercase letters in your password? Yes or No")
    ifu = input()
    if ifu == 'Yes':
        chars += uppercase_letters
        
    print("Do you want punctuation signs in your password? Yes or No")
    ifp = input()
    if ifp == 'Yes':
        chars += punctuation
            
    print("Do you want such easily messed up signs like 'il1Lo0O' in your password? Yes or No")
    ifm = input()
    if ifm == 'No':
        new_chars = ''
        for c in chars:
            if c not in messup:
                new_chars += c
        chars = new_chars
        
    print(generate_password(length, chars))
