# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define dis_slow = Dissolve(0.5)
define dis_fast = Dissolve(0.1)
define i = Character("Isabelle")
define rik = Character("Rika", color="#ff8000")
define e = Character("Elizabeth", color="#ff8aef")
define mc = Character("You", color="#007bff")
define t = Character("Teacher")
define suc = Character("Success")
define fail = Character("Fail")

# Declare Music
define audio.bgm1 = "music/freetime_bgm.mp3"
define audio.bgm2 = "music/class_bgm.mp3"
define audio.bgm3 = "music/exam_bgm.mp3"
define audio.bgm4 = "music/class2_bgm.mp3"
define audio.bgm5 = "music/elizabeth_bgm.mp3"
define audio.bgm6 = "music/rika_bgm.mp3"
define audio.bgm7 = "music/isabelle_bgm.mp3"
define audio.bgm8 = "music/past_bgm.mp3"
define audio.se1 = "music/typing_se.mp3"
define audio.se2 = "music/diceroll_se.mp3"
define audio.se3 = "music/crowd_se.mp3"
define audio.se4 = "music/win_se.mp3"
define audio.se5 = "music/lose_se.mp3"
define audio.se6 = "music/writing_se.mp3"
# initializations (class, variables, etc.)
init python:
    # player 'currencies'
    intelligence = 0
    isk = 0
    # player status
    stamina = 40
    mental_health = 40
    # tm is variable for storing time, initialized here
    tm = 7
    day = 1
    normal_days_count = 0
    exam_days_count = 0
    # so player cannot keep clicking on missed class
    click = 0
    # click2 so player forced to press missed class
    click2 = 0
    score_player = 0
    score_opponent = 0
    finalshowdown = 0
    # Elizabeth y align
    e_yalign = -1.2
    # Rika y align
    r_yalign = -1.35
    # Isabelle y align
    i_yalign = -0.75

    # Story master y modifier, add variable to default yalign
    sm_ymodifier = -0.5
    # Position character to left
    sm_x = -.05
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

    screen clock:
        modal False
        frame:
            style "screen_background"
            xalign 0.5
            yalign 0.0

            xsize 150
            ysize 50


            text "[tm]"+":00" xalign 0.5 yalign 0.5

    screen day:
        modal False
        frame:
            style "screen_background"
            xalign 0.5
            yalign 0.06

            text "Day [day]" xalign 0.75 yalign 0.0

    screen currency:
        modal False
        frame:
            style "screen_background"
            xalign 0.5
            yalign 0.12 #previous value = 0.06
            vbox:
                text "Intelligence Pts." xalign 0.5 size 25
                text "[intelligence]" xalign 0.5 size 20
                text "Is-She-Kay Pts." xalign 0.5 size 25
                text "[isk]" xalign 0.5 size 20
                text "GPA" xalign 0.5 size 25
                text "[GPA]" xalign 0.5 size 20


    show screen clock
    $ fd = "first_day"
    call expression fd from call1

    show screen currency
    show screen clock

    $ ft = "free_time"
    call expression ft from _call_expression
