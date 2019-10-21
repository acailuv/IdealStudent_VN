label exams:
    show classroom2 with dis
    hide screen actions
    hide classroom
    hide tidyroom
    $ perf_score_cost = (normal_days_count - exam_days_count)*800
    $ pass_score_cost = (normal_days_count - exam_days_count)*700
    # To prevent the score cost to be negative
    if (perf_score_cost < 0):
        $ perf_score_cost = 0
    if (pass_score_cost < 0):
        $ pass_score_cost = 0
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

    "You got a 100 on your exam"
    $ intelligence = intelligence - perf_score_cost
    $ GPA = GPA + 0.2
    jump choice_done

label choice_pass:

    "You passed your exam"
    $ intelligence = intelligence - pass_score_cost
    jump choice_done

label choice_fail:
    "You failed your exam"
    $ GPA = GPA - 0.2
    jump choice_done

label choice_done:

    hide classroom2
    $ chance = renpy.random.randint(1,10)
    $ tm = 17
    jump free_time
