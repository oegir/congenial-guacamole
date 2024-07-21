# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#238c00")
define v = Character("Vasil", color="#002699")
define vi = Character("Vasilina", color="#ff80ff")


# The game starts here.

label start:

    scene bg room

    show eileen happy

    v "Hello, World. I am Vasil."

    vi "Hi, Vasya. I laid an egg."

    "Long ago, Vasil and Vasilina met."

    return
