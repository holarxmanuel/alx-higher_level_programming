#!/usr/bin/python3
import random

num = random.randint(-10000, 10000)

if num < 0:
    non_negative = num * -1
else:
    non_negative = num

lst = non_negative % 10

if lst > 5:
    print(f"Last digit of {num:d} is {lst:d} and is greater than 5")
elif lst == 0:
    print(f"Last digit of {num:d} is {lst:d} and is 0")
else:
    print(f"Last digit of {num:d} is {lst:d} and is less than 6 and not 0")
