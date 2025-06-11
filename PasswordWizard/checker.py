score = 0
shortcomings = []


def main(password=None):
    global score, shortcomings

    password = password if password else input("Password: ")

    lengthChecker(password)
    alphabetChecker(password)
    numberChecker(password)
    specialCharChecker(password)

    
    match score:
        case 5:
            print(f"Strength Score: {score}\n"
                  "Result:         oustanding")
        case 4:
            print(f"Strength Score: {score}\n"
                  "Result:         Excedes Expectation")
        case 3:
            print(f"Strength Score: {score}\n"
                  "Result:         Acceptable")
        case 2:
            print(f"Strength Score: {score}\n"
                  "Result:         Poor")
        case 1:
            print(f"Strength Score: {score}\n"
                  "Result:         Troll")
        case _:
            print('Invalid Input')
    print()
        
    if shortcomings:
        print('Points to improve')
        for i in range(len(shortcomings)):
            print(i+1, shortcomings[i])
        print()

def lengthChecker(password):
    global score, shortcomings
    passwordLength = len(password)
    if passwordLength >= 12:
        score += 1
    else:
        shortcomings.append('Password should be atleast 12 characters long.')


def  alphabetChecker(password):
    global score, shortcomings
    upperFlag = lowerFlag = False
    for l in password:
        if l.isalpha():
            if l.islower():
                lowerFlag = True
                continue
            if l.isupper():
                upperFlag = True
                continue

    if upperFlag:
        score += 1
    else:
        shortcomings.append('Password must conatin atleast one uppercase character.')
    
    if lowerFlag:
        score += 1
    else:
        shortcomings.append('Password must conatin atleast one lowercase character.')


def numberChecker(password):
    global score, shortcomings
    numberFlag = False

    for l in password:
        if l.isdecimal():
            numberFlag = True
            break
    
    if numberFlag:
        score += 1
    else:
        shortcomings.append('Password must conatin atleast one numerical character')


def specialCharChecker(password):
    global score, shortcomings
    specialFlag = False
    specialCharacters = [
        '`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '-', '_', '=', '+', '[', ']', '{', '}',
        '|', ';', ':', ',', '<', '.', '>', '/', '?'
    ]

    for l in password:
        if l in specialCharacters:
            specialFlag = True
            break
    
    if specialFlag:
        score += 1
    else:
        shortcomings.append('Password must conatin atleast one special character')


if __name__ == '__main__':
    main()