import random

lower_case = "abcdefghijklmnopqrstuvwxys"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "@#$%^&*/\?"

Use_for = lower_case + upper_case + number + symbol
length_for_pass = 8

password = "".join(random.sample(Use_for, length_for_pass))

print("Your generated password is: " + password)