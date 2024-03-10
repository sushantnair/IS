def calc(plaintext, noc):
    print('--------------------------------------------------------------')
    print('Keyless Columnar Cipher')
    print(f'Plaintext: {plaintext}')
    print(f'Number of Columns: {noc}')
    table = list()
    for i in range(0, len(plaintext), noc):
        table.append(plaintext[i:i+noc])
    for item in table:
        print(item)
    cipher = encrypt(table, noc)
    print ("Cipher:", cipher)
    nor = round(len(plaintext) / noc)
    plain = decrypt(cipher, table, nor, noc)
    print ("Plain:", plain)

def encrypt(table, noc):
    encrypted = ""
    # Iterating over the columns in the order specified by the key
    for i in range(0, noc + 1):
        # Appending the characters in the column to the output
        try:
            column = [row[i] for row in table if len(row) >= i]
        except:
            continue
        encrypted += "".join(column)
    # Returning the output
    return encrypted

def decrypt(encrypted, nor, noc):
    # Creating an empty matrix to store the transposition of the encrypted text
    transposed_matrix = [[''] * noc for _ in range(nor)]
    # print(transposed_matrix)
    # Filling the matrix with the encrypted text
    idx = 0
    for i in range(noc):
        col = i
        for j in range(nor):
            if idx < len(encrypted):
                transposed_matrix[j][col] = encrypted[idx]
                idx += 1
    # print(transposed_matrix)
    decrypted = ""
    for row in transposed_matrix:
        decrypted += ''.join(row)
    return decrypted