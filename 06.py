# Importing modules
# On peut avoir plusieurs modules importer séparé par des virgules
# Exemple d'un état import avec plusieurs modules séparé par des virgules
import random, sys, os, math
import random
for i in range(5):
    print(random.randint(1, 10))

# Autre façon d'importer des modules
# Différence: avec cette façon d'import module tu n'a pas besoin de spécifier le préfixe random. 
from random import randint
from random import *

for i in range(5):
    print(randint(1,10))



import sys
#from sys import *
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
    # Permet de terminer le programme
        sys.exit()
        #exit()
    print('You typed ' + response + '.')

#9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
#Greetings! if anything else is stored in spam.

spam = 1
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
#program that prints the numbers 1 to 10 using a while loop.

print('Boucle for')
for i in range(10):
    print(i)

print('boucle while')
i = 0
while i < 10:
    print(i)
    i = i + 1