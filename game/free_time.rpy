label free_time:
    # Variables
    $ stamina = 40
    $ mental_health = 40

    # Screen configurations
    screen stats():
        modal True
        frame:
            background Solid("#0000009B")

            xsize 450
            ysize 300

            xalign 1.0
            yalign 0.0

            xpadding 25
            ypadding 25

            vbox:
                text "{b}{u}Stats{/u}{/b}" xalign 0.5
                null height 20
                text "Stamina ([stamina]/100)"
                bar:
                    value AnimatedValue(stamina, 100, 0.5)
                    left_bar "#ffc130"
                    right_bar "#cc9b27"
                null height 20
                text "Mental Health ([mental_health]/100)"
                bar:
                    value AnimatedValue(mental_health, 100, 0.5)
                    left_bar "#146eff"
                    right_bar "#1058cc"

    screen actions():
        frame:
            background Solid("#0000009B")

            xsize 350
            ysize 250

            xalign 1.0
            yalign 0.4

            xpadding 25
            ypadding 25
            vbox:
                text "{b}{u}Actions{/u}{/b}" xalign 0.5
                null height 20
                hbox:
                    xalign 0.5
                    vbox:
                        text "{u}Restore{/u}"
                        button:
                            text "Sleep" style "button_text" xalign 0.5
                            action [
                                    Notify("Sleeping..."),
                                    SetVariable("tm", t.addTime(7))
                            ]
                        button:
                            text "Rest" style "button_text" xalign 0.5
                            action Notify("Resting...")
                    null width 30
                    vbox:
                        text "{u}Improve{/u}"
                        button:
                            text "Study" style "button_text" xalign 0.5
                            action Notify("Studying...")
                        button:
                            text "Practice" style "button_text" xalign 0.5
                            action Notify("Practicing [Is-She-Kay Life]...")
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
