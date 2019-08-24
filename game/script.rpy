# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Isabelle")
define r = Character("Rika", color="#ff8000")
define e = Character("Elizabeth", color="#ff8aef")
define mc = Character("You", color="#007bff")


# The game starts here.

label start:

    # Example screen tinting (to make night scene)
    # image nightRoomTidy = im.MatrixColor(
    #     "tidyroom bg.png",
    #     im.matrix.tint(0.5, 0.5, 0.8))
    #
    # show nightRoomTidy
    # mc "Hello"

    scene tidyroom
    mc "Yes! I'm almost there! 30 more weekdays and I'll be graduating from this university."
    mc "..."
    mc "It's saturday, maybe I should start making my CV so that I can look for jobs right away!"
    scene black
    "{i}You are writing your CV for hours.{/i}"
    scene tidyroom
    mc "Let's see here, Organizational Experience.... OH NO!"
    mc "I haven't joined a single club or even participate in a seminar from the first time I got here!"

    return
