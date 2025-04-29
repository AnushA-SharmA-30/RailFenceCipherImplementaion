def encrypt_rail_fence(text, key):
    if key <= 1:
        return text

    # Create the rail matrix
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]

    direction_down = False
    row = 0

    # Populate the rail matrix in zig-zag manner
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][i] = text[i]

        row += 1 if direction_down else -1

    # Construct the result by reading the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return ''.join(result)


def decrypt_rail_fence(cipher, key):
    if key <= 1:
        return cipher

    # Create the rail matrix
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    # Mark the places to be filled
    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        row += 1 if direction_down else -1

    # Fill the rail matrix with the cipher characters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Now read the matrix in zig-zag manner to construct the original message
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        row += 1 if direction_down else -1

    return ''.join(result)


# Example usage
if __name__ == "__main__":
    text = input("Enter plain text: ")
    key = int(input("Enter key(>1): "))

    encrypted = encrypt_rail_fence(text, key)
    print("Encrypted:", encrypted)

    decrypted = decrypt_rail_fence(encrypted, key)
    print("Decrypted:", decrypted)
