# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Isabelle")
define r = Character("Rika", color="#ff8000")
define e = Character("Elizabeth", color="#ff8aef")
define mc = Character("You", color="#007bff")

# initializations (class, variables, etc.)
init python:
    # player 'currencies'
    intelligence = 0
    isk = 0

    # player status
    stamina = 40
    mental_health = 40

    # Time object for clock
    class Time(object):
        def __init__(self):
            self.t = 7

        def addTime(self, n):
            self.t = (self.t+n)%24
            return self.getTime()

        def getTime(self):
            return str(self.t) + ":00"

# The game starts here.

label start:

    # Custom Styles
    # /////////////
    style screen_background:
        background Solid("#0000009B")

    # Example screen tinting (to make night scene)
    # ////////////////////////////////////////////
    # image nightRoomTidy = im.MatrixColor(
    #     "tidyroom bg.png",
    #     im.matrix.tint(0.5, 0.5, 0.8))
    #
    # show nightRoomTidy
    # mc "Hello"

    # Example if-else control flow in renpy
    # /////////////////////////////////////
    # scene tidyroom
    # mc "Yes! I'm almost there! 30 more weekdays and I'll be graduating from this university."
    # mc "..."
    # mc "It's saturday, maybe I should start making my CV so that I can look for jobs right away!"
    # scene black
    # "{i}You are writing your CV for hours.{/i}"
    # "What are you going to write next?"
    # label ch:
    #     if not pa and not oe:
    #         menu:
    #             "Personal Achievements.":
    #                 jump pa
    #             "Organizational Experience.":
    #                 jump oe
    #     elif pa and not oe:
    #         menu:
    #             "Organizational Experience.":
    #                 jump oe
    #     elif oe and not pa:
    #         menu:
    #             "Personal Achievements.":
    #                 jump pa
    #     else:
    #         return
    #
    #     label pa:
    #         if not pa:
    #             "{i}Huge pride fills your heart as you typed in your current GPA. Which is (something).{/i}"
    #             $ pa = True
    #             jump ch
    #
    #     label oe:
    #         if not oe:
    #             mc "Let's see here, Organizational Experience.... OH NO!"
    #             mc "I haven't joined a single club or even participate in a seminar from the first time I got here!"
    #             $ oe = True
    #             jump ch
    #
    # scene tidyroom

    $ t = Time()
    $ tm = t.getTime()
    screen clock:
        modal False
        frame:
            style "screen_background"
            xalign 0.5
            yalign 0.0

            xsize 150
            ysize 50

            text "[tm]" xalign 0.5 yalign 0.5

    screen currency:
        modal False
        frame:
            style "screen_background"
            xalign 0.5
            yalign 0.06
            vbox:
                text "Intelligence Pts." xalign 0.5 size 25
                text "[intelligence]" xalign 0.5 size 20
                text "Is-She-Kay Pts." xalign 0.5 size 25
                text "[isk]" xalign 0.5 size 20

    show screen clock
    show screen currency
    scene classroom2
    "test"

    $ ft = "free_time"
    call expression ft from _call_expression
