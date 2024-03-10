def calc(plaintext, keyword):
    print('--------------------------------------------------------------')
    print('Key Columnar Cipher')
    print(f'Plaintext: {plaintext}')
    print(f'Keyword: {keyword}')
    noc = len(keyword)
    # number of columns is the length of keyword (i.e., n)
    print(f'Length of Keyword (number of columns): {noc}')
    # Convert the keyword to uppercase
    caps_kw = keyword.upper()
    # order of alphabets in keyword
    ooaik = ''
    # Create a dictionary to store the order of each alphabet in the keyword
    alphabet_order = {char: str(i + 1) for i, char in enumerate(sorted(set(caps_kw)))}
    # Iterate through each letter in capitalized keyword
    for letter in caps_kw:
        # Append the order to the result string
        ooaik += alphabet_order[letter]
    print(f'Order of alphabets in {keyword}: {ooaik}')
    # number of rows
    nor = round(len(plaintext) / noc)
    table = list()
    # Loop through the strings and print them in a table format
    for s in (keyword, ooaik, plaintext):
        # Loop through the slices of four characters and print them on separate lines
        for i in range(0, len(s), noc):
            table.append(s[i:i+noc])
    for item in table:
        print(item)
    cipher = encrypt(table)
    print ("Cipher:", cipher)
    plain = decrypt(cipher, table, nor)
    print ("Plain:", plain)

def encrypt(table):
    # Extracting the key from the second row of the table
    key = table[1]
    # Removing the first and second rows from the table
    table = table[2:]
    # Creating a dictionary to store the order of columns
    order = {int(key[i]): i for i in range(len(key))}
    # Creating an empty string to store the output
    encrypted = ""
    # Iterating over the columns in the order specified by the key
    for i in range(1, len(key) + 1):
        # Appending the characters in the column to the output
        column = [row[order[i]] for row in table if len(row) >= i]
        encrypted += "".join(column)
    # Returning the output
    return encrypted

def decrypt(encrypted, table, nor):
    # Extracting the key from the second row of the table
    key = table[1]
    # Removing the first and second rows from the table
    table = table[2:]
    # Creating a dictionary to store the order of columns
    order = {int(key[i]): i for i in range(len(key))}
    # print(order)
    # Creating an empty matrix to store the transposition of the encrypted text
    transposed_matrix = [[''] * len(key) for _ in range(nor)]
    # print(transposed_matrix)
    # Filling the matrix with the encrypted text
    idx = 0
    for i in range(len(key)):
        col = order[i + 1]
        for j in range(nor):
            if idx < len(encrypted):
                transposed_matrix[j][col] = encrypted[idx]
                idx += 1
    # print(transposed_matrix)
    # Constructing the decrypted text by reading rows from the transposed matrix
    decrypted = ""
    for row in transposed_matrix:
        decrypted += ''.join(row)
    return decrypted