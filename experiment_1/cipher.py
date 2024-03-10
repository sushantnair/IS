import keycc, keylesscc, pfc

def main():
    print('--------------------------------------------------------------')
    print('------------------------CIPHER PROGRAM------------------------')
    print('--------------------------------------------------------------')
    print('\nEnter 1 for Key Columnar Cipher')
    print('\nEnter 2 for Keyless Columnar Cipher')
    print('\nEnter 3 for Playfair Cipher')
    ch = int(input('Enter your choice: '))

    plaintext = input('Enter the Plain Text (hit 1 key for SUSHANT and 2 key for Geeks for Geeks): ').upper()
    if plaintext == "1":
        plaintext = "SUSHANT"
    elif plaintext == "2":
        plaintext = "Geeks for Geeks"

    keyword = input('Enter the Keyword (hit 1 key for HACK and 2 key for SECURITY): ').upper()
    if keyword == "1":
        keyword = "HACK"
    elif keyword == "2":
        keyword = "SECURITY"

    if ch == 1:  
        keycc.calc(plaintext, keyword)
    elif ch == 2:
        noc = int(input('Enter the number of columns for encryption: '))
        keylesscc.calc(plaintext, noc)
    elif ch == 3:
        pfc.calc(plaintext, keyword)
    else:
        print('Incorrect choice entered.')

if __name__ == "__main__":
    main()