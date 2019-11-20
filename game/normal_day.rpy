label normal_day:
    hide screen actions
    hide classroom2
    hide classroom
    hide tidyroom
    "...."

    show classroom2 with dis_slow
    play music bgm5
    $ rndm = renpy.random.randint(0,3)
    if rndm == 0:
        t"Class dismissed!"
        mc"Finally!"
    elif rndm == 1:
        t"And so, 1+1 is equals to 2."
        t"This is going to be in the exam!"
        mc"-_-"
    elif rndm == 2:
        t"Don't forget to study we've got a surprise exam soon!"
        mc"*whispers* Why do you even tell us this when we don't even know when the exam is."
        t"*???* Did someone say something?"
        mc"Sh- Nothing teach, have a great day."
    else:
        t"Ok I think that's it for today. Any questions?"
        mc"Yes, can I know when we're having the test?"
        t"It's called a surprise exam for a reason"
        mc"Ugh..."
    "You gained 700 Intelligence Points for attending today's class."
    $ intelligence = intelligence + 700
    $ chance = renpy.random.randint(1,10)
    $ tm = 17
    stop music fadeout 1.0
    play music bgm1 fadein 1.0
    jump free_time
