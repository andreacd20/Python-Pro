# import random

# char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# length = int(input("Pass length:"))

# password = ""

# for i in range(length):
#     password += random.choice(char)

# print(password)

from bot_logic import gen_pass

print(gen_pass(10))