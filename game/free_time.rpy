label free_time:
    # Screen configurations
    screen stats():
        modal True
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
        frame:
            background Solid("#0000009B")

            xsize 275
            ysize 200

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
                            if stamina<=20 and mental_health<=20:
                                action [
                                    Notify("Sleeping..."),
                                    SetVariable("tm", t.addTime(7)),
                                    SetVariable("stamina", stamina+80),
                                    SetVariable("mental_health", mental_health+80)
                                ]
                            elif stamina<100 and mental_health<100:
                                action [
                                    Notify("Sleeping..."),
                                    SetVariable("tm", t.addTime(7)),
                                    SetVariable("stamina", 100),
                                    SetVariable("mental_health", 100)
                                ]
                        button:
                            text "Rest" style "button_text" size 25
                            if stamina<=90 and mental_health<=85:
                                action [
                                    Notify("Resting..."),
                                    SetVariable("tm", t.addTime(1)),
                                    SetVariable("stamina", stamina+10),
                                    SetVariable("mental_health", mental_health+15)
                                ]
                            elif stamina<100 and mental_health<100:
                                action [
                                    Notify("Resting..."),
                                    SetVariable("tm", t.addTime(1)),
                                    SetVariable("stamina", 100),
                                    SetVariable("mental_health", 100)
                                ]
                    null width 20
                    vbox:
                        text "{u}Improve{/u}" size 25
                        button:
                            text "Study" style "button_text" size 25
                            if stamina>=30 and mental_health>=30:
                                action [
                                    Notify("Studying..."),
                                    SetVariable("tm", t.addTime(3)),
                                    SetVariable("stamina", stamina-30),
                                    SetVariable("mental_health", mental_health-30),
                                    SetVariable("intelligence", intelligence+200)
                                ]
                            else:
                                action Notify("Not Enough Stamina or Mental Health")
                        button:
                            text "Practice" style "button_text" size 25
                            if stamina >= 10 and mental_health >= 30:
                                action [
                                    Notify("Practicing [Is-She-Kay Life]..."),
                                    SetVariable("tm", t.addTime(3)),
                                    SetVariable("stamina", stamina-10),
                                    SetVariable("mental_health", mental_health-30),
                                    SetVariable("isk", isk+200)
                                ]
                            else:
                                action Notify("Not Enough Stamina or Mental Health")
            # Debug button Example
            # ////////////////////
            # button:
            #     text "+Stats" style "button_text"
            #     action [
            #         SetVariable("stamina", If(stamina<=90, stamina+10, 100)),
            #         SetVariable("mental_health", If(mental_health<=90, mental_health+10, 100)),
            #         Notify("+Stamina; +Mental Health")
            #     ]
    show screen stats
    show screen actions

    show tidyroom
    "What should I do...."
