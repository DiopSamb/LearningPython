# break statement
# condition is True, it enters in the while loop
# Dans le cas la condition est True dans un boucle while, il entre dans la boucle
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# example or condition is False and once it doesn't enter in the while loop
# Dans le cas ou la condition est False dans la boucle while, on sort directe de la boucle
while False:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')