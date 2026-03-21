import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

password = ''
for x in range(16):
    password += random.choice(chars)

print(f"Password: {password}")
