'''
Write a Python program that searches through a list of randomly generated numbers (1 - 100), looking for 42.
The list you generate should be 500 numbers long.

If 42 Exists in List
Print "I found the meaning of life!"

If 42 Doesn't Exist in List
Print "I did not find the meaning of life!"
'''
import random

google_off_temu_or_wish = []

for i in range(25):
    x = random.randint(1,100)

    google_off_temu_or_wish.append(x)


for i in range(25):
    if google_off_temu_or_wish[i] == 42:
        print('I have found the meaning of life!')
        exit(0)
        

print('I have not found the meaning of life.')

