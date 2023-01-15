import random

a = '''qwertyuiopasdfghjkl@#[]<>ZxzcvbnmQWERTYUIOPASDFGHJJKLZMXNVBC1234567890@?^ì''' 

i = int(input("quanto deve essere lunga la password? "))
password = ""
for x in range (i):
    password+=random.choice(a)

print("Questa è una possibile password: ", password)
