import random

pass_len = int(input("Choice the length's password: "))

password = 'abcdefghijklmnopqrstuvwxyz0123456789'

randomizer = ''.join(random.sample(password,pass_len))
print(randomizer)
