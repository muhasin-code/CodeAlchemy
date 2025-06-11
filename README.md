# CodeAlchemy
CodeAlchemy is a public GitHub repository maintained by Muhammed Muhasin. It features a collection of thoughtfully crafted coding solutions aimed at finding code solutions for challenging tasks.


## PasswordWizard
PasswordWizard is a directory that contains three Python files. These three Python files can generate passwords and check the strength of a password.

### Files in the directory
**First Commit: 11 - Jun - 2025**

#### checker.py
This Python file check the strength of an inputted password. The strength will be checked against 5 criterias. They are:

1. Password length >= 12 characters.
2. Atleast one lowercase character.
3. Atleast one uppercase character.
4. Atleast one numerical character.
5. Atleast one special character.

There are five strength levels. They are (in ascending order of strength):

1. Score: 1 -> Troll: Weakest password.
2. Score: 2 -> Poor: Better than troll but still weak.
3. Score: 3 -> Acceptable: Password of intermediate strength.
4. Score: 4 -> Exceeds Expectations: A password of good strength.
5. Score: 5 -> Outstanding: The best password.

The program will show stregth score and based on the score it will also give points improve your password. The number of improvement advices will decrease with ascending strenth score. It means, score 5 will have no advice point, and score 1 will have 5 advice points. They are:

1. Password should be atleast 12 characters long.
2. Password must conatin atleast one uppercase character.
3. Password must conatin atleast one lowercase character.
4. Password must conatin atleast one numerical character.
5. Password must conatin atleast one special character.


#### password_generator.py
This Python file generates a password. The password may contain uppercase, lowercase, numerical, and special characters. The length of the password is less than 12.


#### test_system.py
This file integrates the *checker.py* and *password_generator.py* files to automatically generate a password of varying length and checks the strength of the generated password. It automates the purpose.

If you are using this file to automates the generation and checking activities, then the password length will no longer be 12 but it will be less than 89.