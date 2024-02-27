message = input("Please enter your message: ")
key = int(input("Please enter the key: "))


def encrypt_text(message, key):
    result = ""
    for i in range(len(message)):
        letter = message[i]

        if letter == " ":
            result += " "

        elif letter == ".":
            result += "."

        elif (letter.isupper()):
            result += chr((ord(letter) + key-65) % 26 + 65)

        else:
            result += chr((ord(letter) + key-97) % 26 + 97)

    return result


print(encrypt_text(message, key))
