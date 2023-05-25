
# statement continue
# Boucle infinie

# while True:
#     print('Hello word')

# Pour arrêter une boucle infinie, il faut faire CTRL+C


# Statement continue
while True:
    print('Who are you')
    name = input()
    if name != 'joe':
        continue
    print('Hello joe. What is the password ? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')

# Quand tu utilise 0, 0.0 ou ''(caratére vide) dans une condition,
# Il est considéré comme False
name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
# Si la valeur numOfGuests n'est pas égale à  0, la condition est vraie
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')


#Calculer la somme de 0 à 100 du résultats de nombres successive avec son successeur
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1