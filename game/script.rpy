# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Isabelle")
define r = Character("Rika", color="#ffe59e")
define e = Character("Elizabeth", color="#ff8aef")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show i_n at left
    show r_n at right
    show e_n at center

    # These display lines of dialogue.

    # i "Sure, You'll get one."
    # "She points her finger at you."
    # i "If you manage to defeat me in \[Is-She-Kay Life\]. You have 30 days to practice."

    # r "Isabelle! How are you?"
    # i "Fine..."
    # r "Ow man, you are such a downer!"
    # i "{i}sigh...{/i}"

    r "Alright guys! Are you ready???"
    i "Sure."
    e "Let's do this!"
    r "One two-"

    i "Welcome..."
    e "Toooooooo~~"
    r "The Board Game club!!!!~"

    r "Yaaay! Good job everyone!"

    # This ends the game.

    return
