label missed_exam_day:
    hide screen actions
    $ chance = renpy.random.randint(1,10)
    "You misssed an exam"
    "Your GPA goes down"
    $ tm = 17
    $ GPA = GPA - 0.3
    if (GPA < 0):
        $ GPA = 0
    jump free_time

label missed_normal_day:
    hide screen actions
    $ chance = renpy.random.randint(1,10)
    $ tm = 17
    "You missed classes"
    jump free_time

label missed_showdown:
    hide screen actions
    $ tm = 17
    $ chance = renpy.random.randint(1,10)
    "You missed your showdown"
    jump free_time
