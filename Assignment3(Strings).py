# STRINGS
# 1. Write a program that accepts a string from user. Your program should count and display number of
# vowels in that string.
def count_vowels():
    user_input = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in user_input if char in vowels)
    print(f"Number of vowels in the string: {count}")

count_vowels()


# 2. Write a program that reads a string from keyboard and display:
# * The number of uppercase letters in the string
# * The number of lowercase letters in the string
# * The number of digits in the string
# * The number of whitespace characters in the string
def count_character_types():
    user_input = input("Enter a string: ")
    uppercase = sum(1 for char in user_input if char.isupper())
    lowercase = sum(1 for char in user_input if char.islower())
    digits = sum(1 for char in user_input if char.isdigit())
    whitespace = sum(1 for char in user_input if char.isspace())

    print(f"Uppercase letters: {uppercase}")
    print(f"Lowercase letters: {lowercase}")
    print(f"Digits: {digits}")
    print(f"Whitespace characters: {whitespace}")

count_character_types()


# 3. Write a Python program that accepts a string from user. Your program should create and display a
# new string where the first and last characters have been exchanged.
def exchange_first_last():
    user_input = input("Enter a string: ")
    if len(user_input) < 2:
        print("String too short to exchange.")
    else:
        new_string = user_input[-1] + user_input[1:-1] + user_input[0]
        print(f"New string: {new_string}")

exchange_first_last()


# For example if the user enters the string 'HELLO' then new string would be 'OELLH'
# 4. Write a Python program that accepts a string from user. Your program should create a new string in
# reverse of first string and display it.
# For example if the user enters the string 'EXAM' then new string would be 'MAXE'
def reverse_string():
    user_input = input("Enter a string: ")
    reversed_string = ''.join(reversed(user_input))
    print(f"Reversed string: {reversed_string}")

reverse_string()


# 5. Write a Python program that accepts a string from user. Your program should create a new string by
# shifting one position to left.
# For example if the user enters the string 'examination 2021' then new string would be 'xamination
# 2021e'
def shift_left():
    user_input = input("Enter a string: ")
    if len(user_input) < 2:
        print("String too short to shift.")
    else:
        shifted_string = user_input[1:] + user_input[0]
        print(f"Shifted string: {shifted_string}")

shift_left()


# 6. Write a program that asks the user to input his name and print its initials. Assuming that the user
# always types first name, middle name and last name and does not include any unnecessary spaces.
# For example, if the user enters Ajay Kumar Garg the program should display A. K. G.
# Note:Don't use split() method
def print_initials():
    name = input("Enter your full name (first, middle, last): ")
    initials = ""
    for char in name:
        if char.isalpha() and (initials == "" or name[name.index(char) - 1] == " "):
            initials += char.upper() + ". "
    print("Initials:", initials.strip())

print_initials()


# 7. A palindrome is a string that reads the same backward as forward. For example, the words dad,
# madam and radar are all palindromes. Write a programs that determines whether the string is a
# palindrome.
# Note: do not use reverse() method
def is_palindrome():
    user_input = input("Enter a string: ")
    length = len(user_input)
    palindrome = True
    for i in range(length // 2):
        if user_input[i] != user_input[length - i - 1]:
            palindrome = False
            break
    if palindrome:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

is_palindrome()


# 8. Write a program that display following output:
# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT
def display_shifting():
    word = "SHIFT"
    for i in range(len(word)):
        print(word[i:] + word[:i])

display_shifting()


# 9. Write a program in python that accepts a string to setup a passwords. Your entered password must
# meet the following requirements:
# The password must be at least eight characters long.
# It must contain at least one uppercase letter.
# It must contain at least one lowercase letter.
# It must contain at least one numeric digit.
# Your program should should perform this validation.
def validate_password():
    password = input("Enter a password: ")
    if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password)):
        print("Password is valid.")
    else:
        print("Password is invalid.")

validate_password()
