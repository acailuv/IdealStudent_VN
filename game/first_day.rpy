

#########################
#Elizabeth:
#neutral
#Yalign: -0.5
#
#Isabelle:
#neutral
#Yalign: -0.5
#
#Rika:
#neutral
#Yalign: -1.25
#########################

label first_day:
    $ GPA = (renpy.random.randint(0,10) + 30.0) / 10

    #Screen Configurationss
    mc"(I've got a solid GPA of [GPA])"
    mc"(It's only 30 days left before I graduate how gre-)"
    mc"(Oh no! I just remembered I need to get a certificate)"
    mc"(Better check the board)"
    mc"*Checks board*"
    mc"(All clubs are full? No way!)"
    mc"(I'm so dead...)"
    mc"(What's this? There's one slot left for board game club)"
    mc"(Time to get there before someone else takes it)"

    #Introduction to all the characters

    show classroom with dis_slow
    mc"Uh... hello? Is this board game club?"

    show i_neutral with dis_fast:
        xalign 1.0
        yalign i_yalign
    i"Yes. What do you want?"
    i"If I recall correctly I think I have marked this club as full on the club board back at the main hall."
    i"Don't tell me..."
    i"Elizabeth did you mark this club as full on the club board back at the main hall yesterday?"
    show e_shy with dis_fast:
        xalign 0.5
        yalign e_yalign
    e"Oh, I forgot teehee~"
    i"..."
    i"*sigh* Well since it's our bad, welcome to the club I guess... I'm Isabelle."
    show r_neutral with dis_fast:
        xalign 0.675
        yalign r_yalign
    rik"Hello my name is Rika nice to meet you!"
    hide e_shy with dis_fast
    show e_neutral with dis_fast:
        xalign 0.5
        yalign e_yalign
    e"I'm Elizabeth..."

    mc"So does that mean I'll get the certificte when I'm done? I only have 30 weekdays before I graduate."
    i"Sure."
    mc"Phew... Thanks for letting me join this late-"
    show r_neutral with move:
        xalign 1.
        yalign r_yalign
    show e_neutral with move:
        xalign 0.75
        yalign e_yalign
    hide i_neutral with dis_fast
    show i_smile with move:
        xalign 0.2
        yalign i_yalign
    i"Sure, you’ll get one,"
    i "If you beat me at this Is-She-Kay Life board game. You have 30 days to practice"
    mc"You are kidding right? I don’t even know how to play this game!"
    i"You want the certificate or not?"
    mc"*sigh*"
    i"Since we don't have much time every 10 days you will face either Rika or
    Elizabeth"
    hide i_smile with dis_fast
    hide e_neutral with dis_fast
    hide r_neutral with dis_fast
    #Transition to free_time
    $ tm = 17

    show tidyroom with dis_slow

    mc"(Alright I'm back home, looks like I really have to practice playing Is-She-Kay Life)"
    mc"(But I have to make sure my GPA doesn't drop... )"
    mc"(I've got classes at 7:00am tomorrow)"
