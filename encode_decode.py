'''
Title: Lab 06: Github Encoder and Decoder
Author: Thomas Crespo
Date: 07/18/2023
Code Version: Python 3.11
'''

#Simple Encode Function
def encode(password):
    resul = ''
    temp = 0
    for num in password:
        temp = int(num) + 3
        if temp >= 10:
            temp = temp - 10
        resul = resul + str(temp)
    return resul

#Simple Decode Function by Rachel McCallum
def decode(password):
    resul = ''
    temp = 0
    for num in password:
        temp = int(num) - 3
        if temp < 0:
            temp = temp + 10
        resul = resul + str(temp)
    return resul

#The Start of the Looping Encode and Decode Menu
if __name__ == '__main__':
    while True:
        print(
            'Menu\n'
            '-------------\n'
            '1. Encode\n'
            '2. Decode\n'
            '3. Quit\n'
            ''
        )
        option = int(input('Please enter an option: '))
        if option == 1:
            passwor = input('Please enter your password to encode: ')
            enpasswor = encode(passwor)
            print('Your password has been encoded and stored!')
            print()
        elif option == 2:
            depasswor = decode(encode(passwor))
            print('The encoded password is ' + enpasswor +', and the original password is ' + depasswor + '.')
            print()
        elif option == 3:
             break
        else:
            print('Invalid Input')
            continue
        
