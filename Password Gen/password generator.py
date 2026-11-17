import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

password = ''

userinput = int(input("How long do you want your password to be?"))
for x in range(userinput):
    password += random.choice(chars)

print(f"Password: {password}")
