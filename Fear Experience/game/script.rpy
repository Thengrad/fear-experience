# The script of the game goes in this file.

default clock = 8
default fear = 0

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default.

    scene bg room

    # This shows a character sprite. A placeholder is used.
    show eileen happy

    # These display lines of dialogue.

    "Clock informs you that it is [clock]am"
    menu: 
        "You should get up"
        "Get up":
            you "I'm going go be on time but tired"
            $ fear += 20
        "Stay in bed":
            you "I'm late but well rested"
            $ clock += 3
    $ clock += 1
    menu:
        "You need to cash a check"
        "Go to bank":
            you "AHHH. People"
            $fear += 50
        "Use app":
            you "I don't know what i'm doing"
            $fear += 100
    $ clock += 1
    
    menu:
        "You have a paper due"
        "Avoid it and play games":
            you "The paper wasn't good but I feel better"
            $ clock += 4
        "Focus on the paper":
            you "I/'M GOING TO FAIL"
            $ fear += 2000
    $ clock += 1
    
    "It is now [clock]hrs. You have [fear] anxiety"

    # This ends the game.

    return
