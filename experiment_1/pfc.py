def calc(plaintext, keyword):
    print('--------------------------------------------------------------')
    print('Playfair Cipher')
    encrypt(plaintext, keyword)


def generate_key_square(keyword):
   """
   Generates the 5x5 key square using the keyword.
   """
   key_square = [['' for _ in range(5)] for _ in range(5)]
   key_string = keyword + "".join(chr(i) for i in range(65, 91) if chr(i) not in keyword and chr(i) != 'J')
   index = 0
   for i in range(5):
       for j in range(5):
           key_square[i][j] = key_string[index]
           index += 1
   return key_square

def encrypt_pair(pair, key_square):
   """
   Encrypts a pair of letters using the Playfair cipher rules.
   """
   row1, col1 = find_letter_position(pair[0], key_square)
   row2, col2 = find_letter_position(pair[1], key_square)

   if row1 == row2:
       # Same row, shift columns to the right (wrapping around)
       col1 = (col1 + 1) % 5
       col2 = (col2 + 1) % 5
   elif col1 == col2:
       # Same column, shift rows down (wrapping around)
       row1 = (row1 + 1) % 5
       row2 = (row2 + 1) % 5
   else:
       # Different rows and columns, form a rectangle
       col1, col2 = col2, col1

   cipher_text = key_square[row1][col1] + key_square[row2][col2]
   return cipher_text

def decrypt_pair(pair, key_square):
   """
   Decrypts a pair of letters using the Playfair cipher rules.
   """
   row1, col1 = find_letter_position(pair[0], key_square)
   row2, col2 = find_letter_position(pair[1], key_square)

   if row1 == row2:
       # Same row, shift columns to the left (wrapping around)
       col1 = (col1 - 1) % 5
       col2 = (col2 - 1) % 5
   elif col1 == col2:
       # Same column, shift rows up (wrapping around)
       row1 = (row1 - 1) % 5
       row2 = (row2 - 1) % 5
   else:
       # Different rows and columns, form a rectangle
       col1, col2 = col2, col1

   plain_text = key_square[row1][col1] + key_square[row2][col2]
   return plain_text

def find_letter_position(letter, key_square):
   """
   Finds the row and column of a letter in the key square.
   """
   for i in range(5):
       for j in range(5):
           if key_square[i][j] == letter:
               return i, j
   return None  # Letter not found

def prepare_text(text):
   """
   Prepares the text for encryption or decryption by removing spaces and handling double letters.
   """
   text = text.upper()  # Convert to uppercase
   text = text.replace(" ", "")  # Remove spaces
   result = ""
   for i in range(len(text) - 1):
       if text[i] == text[i + 1]:
           result += text[i] + "X"  # Insert 'X' between double letters
       else:
           result += text[i]
   result += text[-1]  # Add the last letter
   if len(result) % 2 == 1:
       result += "Z"  # Add a final 'Z' if needed
   return result

def encrypt(text, key):
    """
    Encrypts the text using the Playfair cipher.
    """
    key_square = generate_key_square(key)
    text = prepare_text(text)
    encrypted_text = ""
    for i in range(0, len(text), 2):
        pair = text[i:i+2]
        cipher_pair = encrypt_pair(pair, key_square)
        encrypted_text += cipher_pair

    print("** Encryption steps for text: " + text + " **")
    print("1. Key square:")
    for row in key_square:
        print("".join(row))
    print("2. Prepared text:", text)
    print("3. Split into pairs:", [text[i:i+2] for i in range(0, len(text), 2)])
    print("4. Encrypted pairs:")
    for i in range(0, len(text), 2):
        print(text[i:i+2], "->", encrypt_pair(text[i:i+2], key_square))
    print("5. Encrypted text:", encrypted_text)
    decrypt(encrypted_text, key)

def decrypt(text, key):
    """
    Decrypts the text using the Playfair cipher.
    """
    key_square = generate_key_square(key)
    decrypted_text = ""
    for i in range(0, len(text), 2):
        pair = text[i:i+2]
        plain_text = decrypt_pair(pair, key_square)
        decrypted_text += plain_text

    print("** Decryption steps for text: " + text + " **")
    print("1. Key square:")
    for row in key_square:
        print("".join(row))
    print("2. Split into pairs:", [text[i:i+2] for i in range(0, len(text), 2)])
    print("3. Decrypted pairs:")
    for i in range(0, len(text), 2):
        print(text[i:i+2], "->", decrypt_pair(text[i:i+2], key_square))
    print("4. Decrypted text:", decrypted_text)
