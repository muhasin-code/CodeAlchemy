from random import randrange, choices


def main():
    generatePassword(12)


def generatePassword(k=None):
    characters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'X', 'Y', 'Z',

        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'x', 'y', 'z',

        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

        '`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '-', '_', '=', '+', '[', ']', '{', '}',
        '|', ';', ':', ',', '<', '.', '>', '/', '?'
    ]

    password = ''

    k = 12 if k else randrange(len(characters))
    passwordCharList = choices(characters, k=k)

    for l in passwordCharList:
        password += l
    
    print(f"\nGenerated Password: {password}\n")
    return password


if __name__ == '__main__':
    main()