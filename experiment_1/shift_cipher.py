chardict = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
    "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
    "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
}

keylst = range(1, 26, 1)

ch = int(input('Enter \'1\' for encryption and \'2\' for decryption: '))

if ch == 1:
    plaintext = input('Enter plaintext for encryption: ').lower()
    key_user = int(input('Enter key: '))
    plaintext = plaintext.replace(' ', '')
    for key in keylst:
        ciphertext = ""
        for character in plaintext:
            # print('Plaintext character: ', character)
            try:
                charval = chardict[str(character)]
            except:
                continue
            # print('Plaintext character value: ', charval)
            ciphercharval = (charval + key) % 26
            # print(plaincharval)
            cipherchar = next((key for key, value in chardict.items() if value == ciphercharval), None)
            # print(plainchar)
            ciphertext += cipherchar if cipherchar else character
        print(f"With key {key}, encrypted text: {ciphertext}")
        if key == key_user:
            print(f"With key {key}, encrypted text: {ciphertext}")
else:
    ciphertext = input('Enter ciphertext for decryption: ').lower()
    ciphertext = ciphertext.replace(' ', '')
    for key in keylst:
        plaintext = ""
        for character in ciphertext:
            # print('Ciphertext character: ', character)
            try:
                charval = chardict[str(character)]
            except:
                continue
            # print('Ciphertext character value: ', charval)
            plaincharval = (charval - key) % 26
            # print(plaincharval)
            plainchar = next((key for key, value in chardict.items() if value == plaincharval), None)
            # print(plainchar)
            plaintext += plainchar if plainchar else character
        print(f"With key {key}, decrypted text: {plaintext}")
            
        