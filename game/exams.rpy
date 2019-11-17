label exams:
    hide screen actions
    hide classroom
    hide tidyroom
    hide classroom2
    "..."
    show classroom2 with dis_slow
    stop music fadeout 1.0
    play music bgm3
    $ perf_score_cost = (normal_days_count - exam_days_count)*800
    $ pass_score_cost = (normal_days_count - exam_days_count)*700
    # To prevent the score cost to be negative
    if (perf_score_cost < 0):
        $ perf_score_cost = 0
    if (pass_score_cost < 0):
        $ pass_score_cost = 0
    t"Alright class we have an exam today!"
    menu:
        "A surprise exam!"
        "Perfect Score
        Cost: [perf_score_cost]":
            if (intelligence >= perf_score_cost):
                jump choice_perf
            else:
                jump choice_fail
        "Pass
        Cost: [pass_score_cost]":
            if (intelligence >= pass_score_cost):
                jump choice_pass
            else:
                jump choice_fail
        "Fail
        Cost: 0":
            jump choice_fail

label choice_perf:
    play sound se6
    "You got a 100 on your exam"
    $ intelligence = intelligence - perf_score_cost
    $ GPA = (GPA + 4)/2
    if GPA > 4:
        $ GPA = 4
    jump choice_done

label choice_pass:
    play sound se6
    "You passed your exam"
    $ intelligence = intelligence - pass_score_cost
    jump choice_done

label choice_fail:
    play sound se6
    "You failed your exam"
    $ GPA = (GPA + 2)/1.75
    if GPA < 0:
        $ GPA = 0
    jump choice_done

label choice_done:

    hide classroom2
    $ chance = renpy.random.randint(1,10)
    $ tm = 17
    stop music fadeout 1.0
    play music bgm1 fadeout 1.0
    jump free_time
