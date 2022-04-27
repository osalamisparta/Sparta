user_prompt = True

while user_prompt:
    age = input ('What is your age? ')
    if age.isdigit() and int(age) > 0 and int(age) <= 120:
        break
    else:
        print('Please provide your age in digits!')

print(f"Your age is: {age}")