print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def list_divisors(number: int) -> list:
    number = int(number)
    mylist = []
    for i in range(1, number + 1, 1):
        if number % i == 0:
            mylist.append(i)
    return mylist


num = int(input('input number '))
print(list_divisors(num))

print("\nQ1b\n")


# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def factors(num1: int, num2: int) -> bool:
    if num1 in list_divisors(num2) or num2 in list_divisors(num1):
        return True
    else:
        return False


print(factors(7, 12))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:
def position(letter: str) -> str:
    return alphabet.index(letter)


letter = input('input letter ')
print(position(letter))

print("\nQ2b\n")


# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def name_pos(name: str):
    string = ""
    for i in range(0, len(name)):
        string = string + str(position(name[i]))
    return string


name = input('Enter name: ')
print(name_pos(name))

print("\nQ2c\n")


# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password(name: str):
    name_id = str(name_pos(name))
    total = int()
    for num in name_id:
        total += int(num)
    total = int(name_id) - total
    return total


print(password('bob'))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def is_prime (num1:int) -> bool:
    count = int(2)
    while count < int(num1) - 1:
        if num1 % count > 0:
            count += 1
        if num1 % count == 0:
            return False
            break



    if count == num1 - 1:
        return True

print(is_prime (11))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:


# -------------------------------------------------------------------------------------- #
