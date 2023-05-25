
# Juste comme python vient avec de nombreux modules
# comme random, math ou time qui produisent des fonctions
# additionnel, la librairie pygame inclut de nombreux modules avec
# des fonctions pour les dessins graphiques, joués des sons,
# manipulés la souris et d'autres.  

# La ligne 1 est une simple déclaration d'importation qui importe les modules |pygame| et |sys|
# afin que notre programme peut utiliser les fonctions qu'ils contiennent. Toutes les fonctions 
# de Pygame traitant du graphisme, du son, et d'autres fonctionnalités fournies par Pygame 
# se trouvent dans le module pygame.
# On peut avoir plusieurs modules importer séparé par des virgules
# Exemple d'un état import avec plusieurs modules séparé par des virgules
import pygame, sys # Ligne #1 


# Autre façon d'importer des modules
# Différence: avec cette façon d'import module tu n'a pas besoin de spécifier le préfixe pygame.locals. 
# Toutefois, avec "from modulename import *", tu peux garder la portion
# "modulename" et simplement utilisé "functionname()" dans ce module (juste comme des fonctions prés établis sur python)


# La raison que vous utiliser ce forme d'import pour pygame.locals est parceque
# pygame.locals contient de nombreux variables constant qui sont facile d'identification
# comme étant dans le module "pygame.locals" sans pygame.locals en début d'eux
# (c'est à dire sans les mettres au début des fonctions "pygame.locals")
# Pour tous les autres modules, tu demandes généralement à utiliser le format régulier "import modulename"

from pygame.locals import * #Ligne #2

# Ligne 4 est l'appel de la fonction "pygame.init()", lequel a besoin toujours d'être appelé
# aprés l'import du module pygame et avant l'appel de tout autre fonctions de pygame.
# Tu n'as pas besoin de connaître que fait cette fonction, tu as juste besoin de connaitre 
# qu'il a besoin d'être appelé en premier dans l'odre pour plusieurs fonctions pygame à travailler.
# Si tu veux regarder un message d'erreur comme "pygame.error: font not initialized"
# Vérifie pour voir si tu oublis d'appeler "pygame.init" au début de ton programme

pygame.init() # Ligne #4


# La ligne 5 est un appel à la fonction pygame.display.set_mode(), qui renvoie le
# Objet pygame.Surface pour la fenêtre. (Les objets de surface sont décrits plus loin dans ce chapitre.)
# Notez que nous passons une valeur de tuple de deux entiers à la fonction : (400, 300). Ce tuple raconte
# la fonction set_mode() détermine la largeur et la hauteur de la fenêtre en pixels. 
# (400, 300) créera une fenêtre d'une largeur de 400 pixels et d'une hauteur de 300 pixels.
# N'oubliez pas de passer un tuple de deux entiers à set_mode(), pas seulement deux entiers eux-mêmes.
# La bonne façon d'appeler la fonction est comme ceci: pygame.display.set_mode((400, 300)).
# Un appel de fonction comme pygame.display.set_mode(400, 300) provoquera une erreur qui
# ressemble à ceci : TypeError : l'argument 1 doit être une séquence de 2 éléments, pas un int.
# L'objet pygame.Surface (nous les appellerons simplement objets Surface en abrégé) renvoyé est
# stocké dans une variable nommée DISPLAYSURF.

DISPLAYSURF = pygame.display.set_mode((400, 300)) # Ligne #5

# La ligne 6 définit le texte de la légende qui apparaîtra en haut de la fenêtre en appelant
# La fonction pygame.display.set_caption(). La valeur de chaîne 'Hello World!' est
# passé dans cet appel de fonction pour faire apparaître ce texte comme légende :

pygame.display.set_caption('Hello World!') # Ligne #6


# Les jeux de ce livre ont tous ces boucles tandis que True en eux avec un commentaire appelant
# c'est la "boucle de jeu principale". Une boucle de jeu (également appelée boucle principale) est une boucle où le code ne
# trois choses:
#   1. Gère les événements.
#   2. Met à jour l'état du jeu.
#   3. Dessine l'état du jeu à l'écran.

# L'état du jeu est simplement une façon de se référer à un ensemble de valeurs pour toutes 
# les variables d'un programme de jeu. Dans de nombreux jeux, l'état du jeu inclut les valeurs 
# des variables qui suivent la santé et la position du joueur, la santé et la position de tous les ennemis,
# quelles marques ont été fait sur un échiquier, le score, ou à qui c'est le tour. 
# Chaque fois que quelque chose se passe comme le joueur subit des dégâts 
# (ce qui réduit leur valeur de santé), ou un ennemi se déplace quelque part, ou quelque chose
# se passe dans le monde du jeu, nous disons que l'état du jeu a changé.
# Si vous avez déjà joué à un jeu qui vous permettait de sauvegarder, 
# l'« état de sauvegarde » est l'état du jeu au moment où vous l'avez sauvegardé. 
# Dans la plupart des jeux, mettre le jeu en pause empêchera l'état du jeu de changer.
# Étant donné que l'état du jeu est généralement mis à jour en réponse à des événements
# (tels que des clics de souris ou des presses) ou le passage du temps, la boucle de jeu vérifie et 
# revérifie constamment plusieurs fois une seconde pour tout nouvel événement qui s'est produit. 
# À l'intérieur de la boucle principale se trouve du code qui regarde quel des événements ont 
# été créés (avec Pygame, cela se fait en appelant la fonction pygame.event.get().
# La boucle principale contient également du code qui met à jour l'état du jeu en fonction 
# des événements qui ont été créé. C'est ce qu'on appelle généralement la gestion des événements.

while True: # main game loop

# Chaque fois que l'utilisateur effectue une action parmi plusieurs 
# (elles sont répertoriées plus loin dans ce chapitre), telles que
# en appuyant sur une touche du clavier ou en déplaçant la souris sur 
# la fenêtre du programme, un objet pygame.event.Event est créé par la 
# bibliothèque Pygame pour enregistrer cet "événement(event)". (C'est un type 
# d'objet appelé Event qui existe dans le module event, qui lui-même est dans le module pygame)
# Nous pouvons savoir quels événements se sont produits en appelant la fonction pygame.event.get (),
# qui renvoie une liste d'objets pygame.event.Event (que nous appellerons simplement Event
# objets pour faire court). La liste des objets d'Event sera pour chaque événement 
# qui s'est produit depuis la dernière fois que La fonction pygame.event.get() a été appelée.
# (Ou, si pygame.event.get() n'a jamais été appelés, les événements qui se sont produits 
# depuis le début du programme.)
    for event in pygame.event.get(): # Ligne 8

# La ligne 8 est une boucle for qui parcourt la liste des objets Event renvoyés par
# pygame.event.get(). À chaque itération de la boucle for, une variable nommée event
# se verra attribuer la valeur du prochain objet Event dans cette liste. 
# La liste des objets Event renvoyés from pygame.event.get() sera dans l'ordre dans 
# lequel les événements se sont produits. Si l'utilisateur a cliqué la souris, puis 
# appuyé sur une touche du clavier, l'objet Event pour le clic de la souris serait le
# premier élément de la liste et l'objet Événement pour l'appui sur le clavier serait 
# le deuxième. Si aucun événement se sont produits, alors pygame.event.get() 
# renverra une liste vide.

        if event.type == QUIT: #Ligne #9
            pygame.quit()
            sys.exit()

# Les objets de Event ont une variable membre (également appelée attributs ou propriétés) nommée "type"
# qui nous indique quel type d'event l'objet représente. Pygame a une variable constante pour chaque
# des types possibles dans les modules pygame.locals. La ligne 9 vérifie si le type de l'objet Event est
# égale à la constante QUIT. N'oubliez pas que puisque nous avons utilisé la forme from pygame.locals
# import * de l'instruction d'importation, nous n'avons qu'à taper QUIT au lieu de
# pygame.locals.QUIT. Si l'objet Event est un événement de sortie, alors les fonctions pygame.quit() et 
# sys.exit() sont appelé. La fonction pygame.quit() est en quelque sorte l'opposé de la fonction pygame.init()
# : elle exécute un code qui désactive la bibliothèque Pygame. Vos programmes doivent toujours 
# appeler pygame.quit() avant d'appeler sys.exit() pour terminer le programme. Normalement non
# vraiment important puisque Python le ferme lorsque le programme se termine de toute façon. 
# Mais il y a un bogue dans IDLE qui provoque le blocage de IDLE si un programme Pygame se termine avant 
# l'appel de pygame.quit(). Comme nous n'avons pas d'instructions if qui exécutent du code pour d'autres types
# d'objets Event, il n'y a pas de code de gestion d'événement lorsque l'utilisateur clique sur la souris, 
# appuie sur les touches du clavier ou provoque tout autre type d'objets Evénement à créer. 
# L'utilisateur peut faire des choses pour créer ces objets Event mais il ne change rien dans le programme 
# car le programme n'a pas de gestion d'événements code pour ces types d'objets Event. Une fois 
# la boucle for sur la ligne 8 terminée, la gestion de tous les événements objets qui ont été retournés
#  par pygame.event.get(), l'exécution du programme continue à la ligne 12.

    pygame.display.update()

# La ligne 12 appelle la fonction pygame.display.update(), qui dessine l'objet Surface
# renvoyé par pygame.display.set_mode() à l'écran (rappelez-vous que nous avons stocké cet objet
# dans la variable DISPLAYSURF). Étant donné que l'objet Surface n'a pas changé (par exemple, par certains
# des fonctions de dessin expliquées plus loin dans ce chapitre), la même image noire est redessinée
# à l'écran chaque fois que pygame.display.update() est appelé.
# C'est tout le programme. Une fois la ligne 12 terminée, la boucle while infinie recommence à partir du
# début. Ce programme ne fait rien d'autre que faire apparaître une fenêtre noire à l'écran,
# vérifie constamment un événement QUIT, puis redessine la fenêtre noire inchangée à l'écran
# encore et encore. Apprenons à faire apparaître des choses intéressantes sur cette fenêtre au lieu de
# juste la noirceur en apprenant les pixels, les objets Surface, les objets Color, les objets Rect et les
# Fonctions de dessin de Pygame.