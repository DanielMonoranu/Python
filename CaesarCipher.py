# 2.CAESAR CIPHER
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "ş", "t",
            "ţ", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "ş", "t", "ţ", "u", "v", "w", "x", "y", "z"]


def cipher(option, string, shift):
    if option == "decrypt":
        shift = -shift

    cipher_text = ""
    for char in string:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
    return cipher_text


end = False
while end is False:
    string = input("Enter a text: ")
    option = input("Enter your choice: 'encrypt' or 'decrypt' ")
    shift = int(input("Enter the shift position number "))
    print(f"Old text: {string}\nNew text: {cipher(option, string, shift)}")
    if input("Enter s to exit or anything else to try again: ") == "s":
        break