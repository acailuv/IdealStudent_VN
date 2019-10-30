label free_time:
    # Screen configurations
    screen stats:
        frame:
            background Solid("#0000009B")

            xsize 450
            ysize 275

            xalign 1.0
            yalign 0.0

            xpadding 25
            ypadding 25

            vbox:
                text "{b}{u}Stats{/u}{/b}" xalign 0.5
                null height 20
                text "Stamina ([stamina]/100)" size 25
                bar:
                    value AnimatedValue(stamina, 100, 0.5)
                    left_bar "#ffc130"
                    right_bar "#cc9b27"
                null height 20
                text "Mental Health ([mental_health]/100)" size 25
                bar:
                    value AnimatedValue(mental_health, 100, 0.5)
                    left_bar "#146eff"
                    right_bar "#1058cc"

    screen actions():
        modal True
        frame:
            background Solid("#0000009B")

            xsize 275
            ysize 250

            xalign 1.0
            yalign 0.35

            xpadding 25
            ypadding 25
            vbox:
                text "{b}{u}Actions{/u}{/b}" xalign 0.5
                null height 20
                hbox:
                    xalign 0.5
                    vbox:
                        text "{u}Restore{/u}" size 25
                        button:
                            text "Sleep" style "button_text" size 25
                            #using more elif conditions for updating time
                            if (tm > 7 and tm < 17 and click == 0):
                                if day == 10 or day == 20 or day == 30:
                                    action [
                                    SetVariable("click", click + 1),
                                    Jump("missed_showdown"), Return(True)]
                                elif chance > 3:
                                    action [
                                    SetVariable("click", click + 1),
                                    SetVariable("normal_days_count", normal_days_count + 1),
                                    Jump("missed_normal_day"), Return(True)]
                                elif chance <= 3:
                                    action [
                                    SetVariable("click", click + 1),
                                    SetVariable("exam_days_count", normal_days_count + 1),
                                    Jump("missed_exam_day"), Return(True)]
                            elif stamina<=20 and mental_health<=20 and tm + 7 < 24:
                                action [
                                    Notify("Sleeping..."),
                                    SetVariable("tm", tm + 7),
                                    SetVariable("stamina", stamina+80),
                                    SetVariable("mental_health", mental_health+80)
                                ]
                            elif stamina<=20 and mental_health<=20 and tm + 7 >= 24:
                                action [
                                    Notify("Sleeping..."),
                                    SetVariable("tm", tm + 7 - 24),
                                    SetVariable("stamina", stamina+80),
                                    SetVariable("mental_health", mental_health+80),
                                    SetVariable("day",day+1),
                                    SetVariable("click",0)
                                ]
                            elif stamina<100 and mental_health<100 and tm + 7 < 24:
                                action [
                                    Notify("Sleeping..."),
                                    SetVariable("tm", tm + 7),
                                    SetVariable("stamina", 100),
                                    SetVariable("mental_health", 100)
                                ]
                            elif stamina<100 and mental_health<100 and tm + 7 >= 24:
                                action [
                                    Notify("Sleeping..."),
                                    SetVariable("tm", tm + 7 - 24),
                                    SetVariable("stamina", 100),
                                    SetVariable("mental_health", 100),
                                    SetVariable("day",day+1),
                                    SetVariable("click",0)
                                ]
                        button:
                            text "Rest" style "button_text" size 25
                            if (tm > 7 and tm < 17 and click == 0):
                                if day == 10 or day == 20 or day == 30:
                                    action [
                                    SetVariable("click", click + 1),
                                    Jump("missed_showdown"), Return(True)]
                                elif chance > 3:
                                    action [
                                    SetVariable("click", click + 1),
                                    SetVariable("normal_days_count", normal_days_count + 1),
                                    Jump("missed_normal_day"), Return(True)]
                                elif chance <= 3:
                                    action [
                                    SetVariable("click", click + 1),
                                    SetVariable("exam_days_count", normal_days_count + 1),
                                    Jump("missed_exam_day"), Return(True)]
                            elif stamina<=90 and mental_health<=85 and tm + 1 < 24:
                                action [
                                    Notify("Resting..."),
                                    SetVariable("tm", tm + 1),
                                    SetVariable("stamina", stamina+10),
                                    SetVariable("mental_health", mental_health+15)
                                ]
                            elif stamina<=90 and mental_health<=85 and  tm + 1 >= 24:
                                action [
                                    Notify("Resting..."),
                                    SetVariable("tm", tm + 1 -24),
                                    SetVariable("stamina", stamina+10),
                                    SetVariable("mental_health", mental_health+15),
                                    SetVariable("day",day+1),
                                    SetVariable("click",0)
                                ]
                            elif stamina<100 and mental_health<100 and tm + 1 < 24:
                                action [
                                    Notify("Resting..."),
                                    SetVariable("tm", tm+1),
                                    SetVariable("stamina", 100),
                                    SetVariable("mental_health", 100)
                                ]
                            elif stamina<100 and mental_health<100 and tm + 1 >= 24:
                                action [
                                    Notify("Resting..."),
                                    SetVariable("tm", tm+1 - 24),
                                    SetVariable("stamina", 100),
                                    SetVariable("mental_health", 100),
                                    SetVariable("day",day+1),
                                    SetVariable("click",0)
                                ]
                            elif (stamina >= 100 and mental_health >= 100):
                                action [
                                    SetVariable("stamina", 100),
                                    SetVariable("mental_health", 100)
                                ]
                                if (tm + 1 >= 24):
                                    action[
                                        Notify("Doing literally nothing"),
                                        SetVariable("tm", tm+1 - 24)
                                    ]
                                else:
                                    action[
                                        Notify("Doing literally nothing"),
                                        SetVariable("tm", tm+1)
                                    ]
                            elif stamina < 100 and mental_health >= 100:
                                action[
                                    SetVariable("mental_health", 100)
                                ]
                                if (tm + 1 >= 24):
                                    action[
                                        Notify("Doing literally nothing"),
                                        SetVariable("tm", tm+1 - 24),
                                        SetVariable("stamina",stamina + 10)
                                    ]
                                else:
                                    action[
                                        Notify("Doing literally nothing"),
                                        SetVariable("tm", tm+1),
                                        SetVariable("stamina",stamina + 10)
                                    ]

                            elif stamina == 100 and mental_health < 100:
                                action[
                                    SetVariable("stamina", 100)
                                ]
                                if (tm + 1 >= 24):
                                    action[
                                        Notify("Doing literally nothing"),
                                        SetVariable("tm", tm+1 - 24),
                                        SetVariable("mental_health",mental_health + 10)
                                    ]
                                else:
                                    action[
                                        Notify("Doing literally nothing"),
                                        SetVariable("tm", tm+1),
                                        SetVariable("mental_health",mental_health + 10)
                                    ]
                            # fix a bug if stamina or mental_health> 100 then player cannot use rest

                    null width 20
                    vbox:
                        text "{u}Improve{/u}" size 25
                        button:
                            text "Study" style "button_text" size 25
                            if (tm > 7 and tm < 17 and click == 0):
                                if day == 10 or day == 20 or day == 30:
                                    action [
                                    SetVariable("click", click + 1),
                                    Jump("missed_showdown"), Return(True)]
                                elif chance > 3:
                                    action [
                                    SetVariable("click", click + 1),
                                    SetVariable("normal_days_count", normal_days_count + 1),
                                    Jump("missed_normal_day"), Return(True)]
                                elif chance <= 3:
                                    action [
                                    SetVariable("click", click + 1),
                                    SetVariable("exam_days_count", normal_days_count + 1),
                                    Jump("missed_exam_day"), Return(True)]
                            elif stamina>=30 and mental_health>=30 and tm + 3 < 24:
                                action [
                                    Notify("Studying..."),
                                    SetVariable("tm",tm+3),
                                    SetVariable("stamina", stamina-30),
                                    SetVariable("mental_health", mental_health-30),
                                    SetVariable("intelligence", intelligence+200)
                                ]
                            elif stamina>=30 and mental_health>=30 and tm + 3 >= 24:
                                action [
                                    Notify("Studying..."),
                                    SetVariable("tm",tm+3-24),
                                    SetVariable("stamina", stamina-30),
                                    SetVariable("mental_health", mental_health-30),
                                    SetVariable("intelligence", intelligence+200),
                                    SetVariable("day",day+1),
                                    SetVariable("click",0)
                                ]

                            else:
                                action Notify("Not Enough Stamina or Mental Health")
                        button:
                            text "Practice" style "button_text" size 25
                            if (tm > 7 and tm < 17 and click == 0):
                                if day == 10 or day == 20 or day == 30:
                                    action [
                                    SetVariable("click", click + 1),
                                    Jump("missed_showdown"), Return(True)]
                                elif chance > 3:
                                    action [
                                    SetVariable("click", click + 1),
                                    SetVariable("normal_days_count", normal_days_count + 1),
                                    Jump("missed_normal_day"), Return(True)]
                                elif chance <= 3:
                                    action [
                                    SetVariable("click", click + 1),
                                    SetVariable("exam_days_count", normal_days_count + 1),
                                    Jump("missed_exam_day"), Return(True)]
                            elif stamina >= 10 and mental_health >= 30 and tm + 3 < 24:
                                action [
                                    Notify("Practicing [Is-She-Kay Life]..."),
                                    SetVariable("tm", tm+3),
                                    SetVariable("stamina", stamina-10),
                                    SetVariable("mental_health", mental_health-30),
                                    SetVariable("isk", isk+200)
                                ]
                            elif stamina >= 10 and mental_health >= 30 and tm + 3 >= 24:
                                action [
                                    Notify("Practicing [Is-She-Kay Life]..."),
                                    SetVariable("tm", tm+3-24),
                                    SetVariable("stamina", stamina-10),
                                    SetVariable("mental_health", mental_health-30),
                                    SetVariable("isk", isk+200),
                                    SetVariable("day",day+1),
                                    SetVariable("click",0)
                                ]

                            else:
                                action Notify("Not Enough Stamina or Mental Health")
                null height 10
                button:
                    # go to university
                    # chance to go to exam is 30%
                    text "Go to University" style "button_text" size 25
                    if tm == 7 and mental_health >= 50 and stamina >= 50:
                        if day == 10 or day == 20 or day == 30:
                            action [Jump("showdown"),Return(True)]
                        elif chance > 3:
                            action [
                                    SetVariable("normal_days_count", normal_days_count + 1),
                                    Jump("normal_day"), Return(True),
                            ]
                        elif chance <= 3:
                            action [
                                    SetVariable("exam_days_count", exam_days_count + 1),
                                    Jump("exams"), Return(True)
                            ]

                    elif (tm > 7 and tm < 17 and click == 0):
                        if day == 10 or day == 20 or day == 30:
                            action [
                            SetVariable("click", click + 1),
                            Jump("missed_showdown"), Return(True)]
                        elif chance > 3:
                            action [
                            SetVariable("click", click + 1),
                            SetVariable("normal_days_count", normal_days_count + 1),
                            Jump("missed_normal_day"), Return(True)]
                        elif chance <= 3:
                            action [
                            SetVariable("click", click + 1),
                            SetVariable("exam_days_count", normal_days_count + 1),
                            Jump("missed_exam_day"), Return(True)]



            # Debug button Example
            # ////////////////////
            # button:
            #     text "+Stats" style "button_text"
            #     action [
            #         SetVariable("stamina", If(stamina<=90, stamina+10, 100)),
            #         SetVariable("mental_health", If(mental_health<=90, mental_health+10, 100)),
            #         Notify("+Stamina; +Mental Health")
            #     ]
    $ chance = renpy.random.randint(1,10)

    show tidyroom with dis_slow
    show screen day
    show screen stats
    show screen actions

    mc"What should I do...."
