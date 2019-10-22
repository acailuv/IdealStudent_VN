

label first_day:
    $ GPA = (renpy.random.randint(0,10) + 30.0) / 10

    #Screen Configurationss
    mc"(I've got a solid GPA of [GPA])"
    mc"(It's only 30 days left before I graduate how gre-)"
    mc"(Oh no! I just remembered I need to get a certificate)"
    mc"(Better check the board)"
    mc"*Checks board"
    mc"(All clubs are full? No way)"
    mc"(I'm so dead...)"
    mc"(What's this? There's one slot left for board game club)"
    mc"(Time to get there before someone else takes it)"

    #Introduction to all the characters

    show classroom with dis
    mc"Uh... hello? Is this board game club?"

    show i with dis:
        xalign 1.0
        yalign 1.0
    i"Yes"
    i"Hi I'm Isabelle"
    show r with dis:
        xalign 0.75
        yalign 1.0
    rik"Hello my name is Rika nice to meet you!"
    show e with dis:
        xalign 0.5
        yalign 1.0
    e"I'm Elizabeth..."

    mc"I was wondering if I could join this late"
    i"Sure"
    mc"Thanks for letting me join this late"
    mc"I am just wondering if I will get a participation certificate or not.
    Since I am joining this late. I really hope you are kind enough to give me that, You see-"
    hide i with dis
    show i_smile with dis:
        xalign 0.2
        yalign 1.0
    i"Sure, you’ll get one,"
    i "If you beat me at this Is-She-Kay Life board game. You have 30 days to practice"
    mc"You are kidding right? I don’t even know how to play this game!"
    i"You want the certificate or not?"
    mc"*Sigh*"
    i"Since we don't have much time every 10 days you will face either Rika or
    Elizabeth"
    hide i_smile with dis
    hide e with dis
    hide r with dis
    #Transition to free_time
    $ tm = 17

    show tidyroom with dis

    mc"(Alright I'm back home, looks like I really have to practice playing Is-She-Kay Life)"
    mc"(But I have to make sure my GPA doesn't drop... )"
    mc"(I've got classes at 7:00am tomorrow)"
