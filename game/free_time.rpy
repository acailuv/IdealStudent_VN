label free_time:
    # Variables
    $ stamina = 40
    $ mental_health = 40

    # Screen configurations
    screen stats():
        modal True
        frame:
            xsize 500
            ysize 500
            xalign 1.0
            vbox:
                text "Stamina ([stamina]/100)"
                bar:
                    value AnimatedValue(stamina, 100, 0.5)
                    left_bar "#ffc34a"
                    right_bar "#cc9b3b"
                null height 20
                text "Mental Health ([mental_health]/100)"
                bar:
                    value AnimatedValue(mental_health, 100, 0.5)
                    left_bar "#69ebff"
                    right_bar "#54bccc"
                null height 50
                button:
                    text "+Stats" style "button_text"
                    action [
                        SetVariable("stamina", If(stamina<=90, stamina+10, 100)),
                        SetVariable("mental_health", If(mental_health<=90, mental_health+10, 100)),
                        Notify("+Stamina; +Mental Health")
                    ]
    show screen stats

    show tidyroom
    ""
