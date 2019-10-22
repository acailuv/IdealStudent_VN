

label showdown:
    hide screen actions
    hide classroom2
    hide classroom
    hide tidyroom
    hide screen stats
    $ score_player = 0
    $ score_opponent = 0
    show screen score
    $ total = 100
    $ tm = 17
    if day == 10:
        $ opponent = 'Elizabeth'
        jump showdown_elizabeth
    elif day == 20:
        $ opponent = 'Rika'
        jump showdown_rika
    else:
        $ opponent = 'Isabelle'
        jump showdown_isabelle

screen score():
    frame:
        xalign 0.5
        xpos 1700
        vbox:
            spacing 10
            text "Your score: [score_player]"
            text "[opponent]'s score: [score_opponent]"

label success:
    if (chance > total/2):
        suc"You rolled [chance] out of [total] you needed a roll greater than 50"
    else:
        fail"You rolled [chance] out of [total] you needed a roll greater than 50"
    menu:
        "Re-roll Cost: 1000":
            $ isk = isk - 1000
            jump success
label showdown_elizabeth:
    show classroom with dis
    show e_flirt with dis:
        xalign 0.5
        yalign 1.0
    e"Hey..."
    e"Let's play!"
    hide e_flirt with dis
    hide classroom
    ###
    $ nullguard = 0
    show city with dis
    "Stage 1"
    $ renpy.pause(0.5)
    "(The monster's population is increasing quite drastically)"
    "(As a result heroes such as you are present to deal with this)"
    "(One Punch is the strongest hero in the Hero Association)"
    "(Unfortunately you are the weakest hero)"
    "(To make up for it you have Hyper Focus to improve yourself)"
    "(Rumors have surfaced stating a monster overlord has been the cause
    of the monster's population increase)"
    "(Many heroes have fallen trying to fight this monster)"
    "(Currently you can train yourself)"
    menu:
        "Learn high-tech computing and immerse yourself in the world of advanced
        robotics and ultra-adaptive articial intelligence":
            jump high_tech_choice

        "Decide to make yourself stronger by learning several hundred types of martial arts":
            jump martial_arts_choice

    label high_tech_choice:
        "Stage 2"
        $ renpy.pause(0.5)
        $ total = 100
        menu:
            "Roll":
                $ chance = renpy.random.randint(1,total)
        "Rolling..."
        $ renpy.pause(0.5)
        # 50 % chance for player
        if (chance > total / 2):
            suc"You  rolled [chance] out of [total] you needed a roll greater than 50"
            "You decided to learn high-tech computing and immerse yourself in the world of advanced robotics and ultra-adaptive
             artificial intelligence. You realized that this is not an easy task even if you have Hyper Focus"
            $ chance = renpy.random.randint(1,total)
            # 80 % chance for elizabeth
            if (chance > 20):
                "She decided to start killing monsters in order to weaken the enemy forces."
                $ score_opponent = score_opponent + 1
            else:
                "She underestimates the game since she got a lucky character. She wanders around
                the world, rising her popularity in this dire situation"
            jump high_tech_choice_2
        else:
            fail"You rolled [chance] out of [total]"
            "You failed to learn high-tech computing"
            if (isk < 1000):
                jump high_tech_choice_2
            else:
                menu:
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump high_tech_choice

                    "Continue":
                        # 80 % chance for elizabeth
                        $ chance = renpy.random.randint(1,total)
                        if (chance > 20):
                            "She decided to start killing monsters in order to weaken the enemy forces."
                            $ score_opponent = score_opponent + 1
                        else:
                            "She underestimates the game since she got a lucky character. She wanders around
                            the world, rising her popularity in this dire situation"
                            jump high_tech_choice_2

    label high_tech_choice_2:
        "Stage 3"
        $ renpy.pause(0.5)
        menu:
            "Roll":
                $ chance = renpy.random.randint(1,total)
        "Rolling..."
        # 60 % chance for player
        if (chance > 60):
            suc"You rolled [chance] out of [total] you needed a roll greater than 60"
            suc"You already mastered the art of making advanced AI and you made
            an exoskeleton that you can use to amplify your weak physical strength. Bravo!"
            $ score_player = score_player + 2
            jump high_tech_choice_3
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 60"
            fail"You tried to use your skill Hyper Focus to study advanced AI and robotics. However, you are unable to
            learn it fast enough. Time is almost up, you can only make standard AI and exoskeleton to aid you in battle."
            if (isk < 1000):
                jump high_tech_choice_3
            else:
                menu:
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump high_tech_choice_2

                    "Continue":
                        $ chance = renpy.random.randint(1,total)
                        # 100 % chance for elizabeth
                        "Since Elizabeth’s character is OP, Elizabeth decided
                        to keep killing monsters to further weaken the enemy forces."
                        $ score_player = score_player + 1
                        $ score_opponent = score_opponent + 1
                        jump high_tech_choice_3

    label high_tech_choice_3:
        "Stage 4"
        $ renpy.pause(0.5)
        menu:
            "Roll":
                $ chance = renpy.random.randint(1,total)
        "Rolling..."
        if (chance > 20 ):
            # 80 % chance for player
            suc"You rolled [chance] out of [total] you needed a roll greater than 20"
            suc"You made a visor with an AI that can analyze your enemies.
             You detected what their weaknesses are and strike them with your exoskeleton."
            $ score_player = score_player + 2
            jump high_tech_choice_4
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 20"
            fail"You made a visor with an AI that can analyze your enemies. However, the enemy you are facing right
            now is very unpredictable, thus your ultra-adaptive AI couldn’t find its weaknesses. You managed to defeat it, though."
            if (isk < 1000):
                jump high_tech_choice_4
            else:
                menu:
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump high_tech_choice_3

                    "Continue":
                        $ chance = renpy.random.randint(1,total)
                        if (chance > 20):
                            # 80 % chance for elizabeth
                            "One Punched."
                            $ score_player = score_player + 1
                            $ score_opponent = score_opponent + 2
                        else:
                            "She underestimated her opponent and got thrown off the area."
                            $ score_player = score_player + 1
                        jump high_tech_choice_4

    label high_tech_choice_4:

        "Stage 5"
        $ renpy.pause(0.5)
        menu:
            "Roll":
                $ chance = renpy.random.randint(1,total)
        "Rolling..."
        if (chance > 50):
            suc"You  rolled [chance] out of [total] you needed a roll greater than 50"
            suc"Thinking that the final boss should have some kind of shield. You successfully made a
            hyper-adaptive device that can nullify any defensive mechanisms. You called it the Null Guard"
            $ score_player = score_player + 1
            $ nullguard = 1
            "Since there isn’t anything Elizabeth can do to improve herself, she can only pass her turn."
            jump high_tech_choice_5
        else:
            "Thinking that the final boss should have some kind of shield. Your adaptive
            AI can’t seem to find a critical point of modelling to make your gadget a reality."
            if (isk<400):
                jump high_tech_choice_5
            else:
                menu:
                    "Re-roll Cost: 400":
                        $ isk = isk - 400
                        jump high_tech_choice_4
                    "Continue":
                        "Since there isn’t anything Elizabeth can do to improve herself, she can only pass her turn."
                        jump high_tech_choice_5

    label high_tech_choice_5:
        "Stage 6"
        $ renpy.pause(0.5)
        if (nullguard == 1):
            suc"You succeed in making Null Guard"
            suc"You defeated the final boss"
            $ score_player = score_player + 3
        else:
            "You failed in making Null Guard"
            "Final boss gets defeateed by Elizabeth's character"
            $ score_opponent = score_opponent + 3
        jump elizabeth_ending

    # martial arts branch


    label martial_arts_choice:
        "Stage 2"
        $ renpy.pause(0.5)
        "You decided to make yourself stronger by learning several hundred types of martial arts."
        "She underestimates the game since she got a lucky character. She wanders around the world,
        rising her popularity in this dire situation. "

        jump martial_arts_choice_2

    label martial_arts_choice_2:
        "Stage 3"
        $ renpy.pause(0.5)
        menu:
            "Roll":
                $ chance = renpy.random.randint(1,total)
        "Rolling..."
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            "Surprisingly, the knowledge of several hundred martial arts and intense training
            made you physically competent. Your physical strength is now equal to the top heroes’ capabilities"
            $ score_player = score_player + 1
            "She decided to start killing monsters in order to weaken the enemy forces."
            $ score_opponent = score_opponent + 1
            jump martial_arts_choice_3
        else:
            "As expected, no matter how much you train, you are still weak. You can kill
             some monsters, but at this rate, there is no hope for you in defeating the final boss commander."
            "She decided to start killing monsters in order to weaken the enemy forces."
            if (isk<1000):
                $ score_opponent = score_opponent + 1
                jump martial_arts_choice_3
            menu:
                "Re-roll Cost: 1000":
                    $ isk = isk - 1000
                    jump martial_arts_choice_2

                "Continue":
                    # 100 % chance for elizabeth
                    $ score_opponent = score_opponent + 1
                    jump martial_arts_choice_3

    label martial_arts_choice_3:
        "Stage 4"
        $ renpy.pause(0.5)
        menu:
            "Roll":
                $ chance = renpy.random.randint(1,total)
        "Rolling..."
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            "You successfully executed the sacred Dragon Waterfall Strike technique on one of the commanders."
            jump martial_arts_choice_4
        else:
            "You have failed to execute the sacred Dragon Waterfall Strike technique on one of the commanders"
            if (isk<1000):
                jump martial_arts_choice_4
            else:
                menu:
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump martial_arts_choice_3

                    "Continue":
                        $ chance = renpy.random.randint(1,total)
                        if (chance > 20):
                            # 80 % chance for elizabeth
                            "One Punched."
                            $ score_opponent = score_opponent + 2
                        else:
                            "She underestimated her opponent and got thrown off the area."
                            $ score_player = score_player + 1
                        jump martial_arts_choice_4
    label martial_arts_choice_4:
        "Stage 5"
        $ renpy.pause(0.5)
        $ chance = renpy.random.randint(1,total)
        if (chance > 75):
            suc"You rolled [chance] out of [total] you needed a roll greater than 75"
            "You feel enlightened and your strength has increased tenfold"
            $ score_player = score_player + 1
            jump martial_arts_choice_5
        else:
            "Thinking that the final boss should have some kind of shield. Your adaptive
            AI can’t seem to find a critical point of modelling to make your gadget a reality."
            if (isk<1000):
                jump martial_arts_choice_5
            else:
                menu:
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump martial_arts_choice_5
                    "Continue":
                        "Since there isn’t anything Elizabeth can do to improve herself,
                         she can only pass her turn."
                        jump martial_arts_choice_4

    label martial_arts_choice_5:
        "Stage 6"
        $ renpy.pause(0.5)
        $ chance = renpy.random.randint(1,total)
        if (chance > 95):
            suc"You rolled [chance] out of [total] you needed a roll greater than 95"
            "You defeated the boss using the Ultimate Sky-Dragon Judgement move"
            $ score_player = score_player + 3
            $ chance = renpy.random.randint(1,10)
            # chance "passed" to free time
            hide screen score
            jump free_time
        else:
            "You failed to defeat the boss"
            if (isk<1000):
                $ score_opponent = score_oppoent + 3
                jump elizabeth_ending
            else:
                menu:
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump martial_arts_choice_5
                    "End":
                        $ score_opponent = score_oppoent + 3
                        jump elizabeth_ending

    label elizabeth_ending:
        $ chance = renpy.random.randint(1,10)
        # chance "passed" to free time
        hide screen score with dis
        hide city with dis
        show classroom with dis
        if (score_player > score_opponent):
            show e_lose with dis:
                xalign 0.5
                yalign 1.0
            e"I lost, even with my overpowered character"
            mc"Hey? What's the matter why so down it was just a game"
            hide e_lose with dis
            show e_sad with dis:
                xalign 0.6
                yalign 1.0
            e"You don't get it"
            e"*Snivel*"
            e"When I was a kid I wore a thick pair of glasses to school"
            e"I would always read comics and enjoyed collecting them"
            e"When I was in fifth grade, my friends would make fun of me"
            e"I was called a nerd for reading comic books"
            e"This goes on till middle school"
            e"When I was in high school I changed my appearance"
            e"I was extremely uncomfortable with it though"
            e"This is why I keep overthinking..."
            e"I don't want people to know I love manga"
            e"I just couldn't take it, so I became someone else in public"
            e"I can't believe I'm telling you this"
            mc"It's fine Elizabeth, I'm happy you told the truth"
            e"You really--"
            mc"Yeah anytime!"
            hide e_sad with dis
            show e_happy with dis:
                xalign 0.7
                yalign 1.0
            e"Thanks hehe"
            e"You know we--"
            e"should...go-"
            mc"back?"
            e"Uhh yeah!"
            e"It's getting kinda late"
            "You gained 2000 Is-She-Kay points for winning"
            hide e_happy with dis
            $ isk = isk + 2000
        elif (score_player < score_opponent):
            e"Better luck next time"
        jump free_time
label showdown_rika:
    show classroom with dis
    show r with dis:
        xalign 0.5
        yalign 1.0
    rik"Hiya!"
    rik"It's time to face me!"
    show r_cheerful with dis:
        xalign 0.5
        yalign 1.0
    hide classroom
    ####
    $ minor_injury = 0
    $ no_fuel = 0
    $ damaged_ship = 0
    $ score_opponent = renpy.random.randint(9,10)
    show space with dis
    "Stage 1"
    $ renpy.pause(0.5)
    "You are at a space bar (not the one located at your keyboard hehe *smack*), you just heard the
    rumor about the “Money Maker”, a device that can make money (or valuable matter including gold and countless more)
     out of thin air."
    "You decided to go through the door. Another muscular merchant pushed you away from the
    door when you are trying to get outside. What are you going to do about this situation"
    menu:
        "Tell the guy that it's not nice pusing people away like that. People could get hurt":
            jump stage_1_rika_bad
        "Just ignore it":
            jump stage_2_rika
    label stage_1_rika_bad:
        $ chance = renpy.random.randint(1,total)
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            "When the big muscular man wants to punch you, he slipped on a space banana. He fell and passed out."
            $ score_player = score_player + 1
            jump stage_2_rika
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 90"
            "The merchant punched you in the gut and you fell to the ground, the whole space bar laugh at your pathetic being."
            if (isk<1000):
                $ score_player = score_player -  1
                $ minor_injury = 1
                jump stage_2_rika
            else:
                if (isk<1000):
                    $ score_player = score_player -  1
                    $ minor_injury = 1
                    jump stage_2_rika
                else:
                    menu:
                        "Re-roll":
                            $ isk = isk - 1000
                            jump stage_1_rika_bad
                        "Continue":
                            $ score_player = score_player -  1
                            $ minor_injury = 1
                            jump stage_2_rika
    label stage_2_rika:
        "Stage 2"
        $ renpy.pause(0.5)
        "You got out from the bar. Time is short, you can either fix the small shallow hole on the side of your
        ship or you can refuel your ship. Remember, your ship is a futuristic, super high tech vehicle."
        menu:
            "Refuel":
                $ damaged_ship = 1
                jump stage_3_rika
            "Fix the shallow hole":
                $ no_fuel = 1
                jump stage_3_rika
    label stage_3_rika:
        "Stage 3"
        $ renpy.pause(0.5)
        "You are done preparing for a long journey, you set sail to the “Money Maker”. Rumor has it that the money maker is
        located at the “Ramvizian System”, 10 light years away from you at the moment."
        "You can either: Enter
        a wormhole (rather unstable) or initiate Hyperspeed drive (stable, but time and resource consuming)"
        menu:
            "Enter a wormhole":
                if (damaged_ship == 1):
                    jump stage_3_rika_damaged_ship
                else:
                    suc"Got through the wormhole safely"
                    $ score_player = score_player + 2
                    jump stage_4_rika

            "Initiate Hyperspeed drive":
                if (no_fuel == 1):
                    jump stage_3_rika_no_fuel
                else:
                    suc"You had enough fuel to get to your destination"
                    $ score_player = score_player + 1

    label stage_3_rika_damaged_ship:
        $ chance = renpy.random.randint(1,total)
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            "Got through the wormhole safely."
            $ score_player = score_player + 2
            jump stage_4_rika
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 90"
            "Your ship can’t handle the harsh nature of the wormhole."
            if(isk<1000):
                $ score_player = score_player - 2
                jump stage_4_rika
            else:
                menu:
                    "Continue":
                      $ score_player = score_player - 2
                      jump stage_4_rika
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump stage_3_rika_damaged_ship

    label stage_3_rika_no_fuel:
        $ chance = renpy.random.randint(1,total)
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            "You had just enough fuel to get to your destination."
            $ score_player = score_player + 1
            jump stage_4_rika
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 90"
            "Your ship can’t handle the harsh nature of the wormhole."
            if(isk<1000):
                jump stage_4_rika
            else:
                menu:
                    "Continue":
                        jump stage_4_rika
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump stage_3_rika_no_fuel
    label stage_4_rika:
        "Stage 4"
        $ renpy.pause(0.5)
        "You landed on the planet where the “Money Maker” resides. Everyone is shooting one another in front of it.
        You have your trusty Laser Blaster with you. You can blast your way past them all to get the
        “Money Maker” or you can go the sneaky beaky way."
        menu:
            "Leeroy Jenkins":
                if (minor_injury == 1):
                    jump stage_4_rika_minor_injury
                else:
                    jump stage_4_rika_no_injury
            "Sneaky Beaky":
                suc"You successfully sneak past them all while they are busy killing each other."
                jump stage_5_rika

    label stage_4_rika_minor_injury:
        $ chance = renpy.random.randint(1,total)
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            "You blast everyone that goes in your way and get your hand on the “Money Maker”"
            $ score_player = score_player + 2
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 90"
            "Ouch! The Injury from the bar fight has gone worse. You can’t go any further."
            if(isk<1000):
                $ score_player = score_player - 2
                jump stage_5_rika
            else:
                menu:
                    "Continue":
                        $ score_player = score_player - 2
                        jump stage_5_rika
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump stage_4_rika_minor_injury

    label stage_4_rika_no_injury:
        $ chance = renpy.random.randint(1,total)
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            "You blast everyone that goes in your way and get your hand on the “Money Maker”"
            $ score_player = score_player + 2
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 90"
            "Your ammunition runs out, you proceed to sneak past them all."
            if(isk<1000):
                jump stage_5_rika
            else:
                menu:
                    "Continue":
                        jump stage_5_rika
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump stage_4_rika_no_injury

    label stage_5_rika:
        "Stage 5"
        $ renpy.pause(0.5)
        "You are a finger away on getting your hands on the “Money Maker”.
        However, your lifetime rival, Rika is there too! You have no choice but to fight her."
        menu:
            "Fight!":
                if (minor_injury == 1):
                    jump stage_5_rika_minor_injury
                else:
                    jump stage_5_rika_no_injury
            "Fight!":
                if (minor_injury == 1):
                    jump stage_5_rika_minor_injury
                else:
                    jump stage_5_rika_no_injury

    label stage_5_rika_minor_injury:
        $ chance = renpy.random.randint(1,total)
        if (chance > 95):
            suc"You rolled [chance] out of [total] you needed a roll greater than 95"
            "Despite your injuries, you relentlessly fought for your own “Money Maker”."
            $ score_player = score_player + 3
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 95"
            "Your Injuries has failed you."
            if(isk<1000):
                jump rika_ending
            else:
                menu:
                    "Continue":
                        jump rika_ending
                    "Re-roll Cost: 1000":
                        jump stage_5_rika_minor_injury

    label stage_5_rika_no_injury:
        $ chance = renpy.random.randint(1,total)
        if (chance > 50):
            suc"You rolled [chance] out of [total] you needed a roll greater than 50"
            "Despite your injuries, you relentlessly fought for your own “Money Maker”."
            $ score_player = score_player + 3
            jump rika_ending
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 50"
            "You failed to get your “Money Maker”"
            if(isk<400):
                jump rika_ending
            else:
                menu:
                    "Continue":
                        jump rika_ending
                    "Re-roll Cost: 400":
                        jump stage_5_rika_no_injury



    label rika_ending:
        show screen classroom with dis
        show r with dis:
            xalign 0.75
            yalign 1.0
        if (score_player>score_opponent):
            show r_surprise with dis:
                xalign 0.6
                yalign 1.0
            rik"That was close!"
            rik"If only I did this instead of that!"
            mc"I still won though"
            hide r_surprise with dis
            show r_happy with dis:
                xalign 0.4
                yalign 1.0
            rik"You're right!"
            rik"Gosh aren't you adorable"
            mc"How are you like this?"
            rik"...."
            hide r_happy with dis
            show r_shy with dis:
                xalign 0.5
                yalign 1.0
            rik"You know two years ago I always smiled"
            rik"I was a very cheerful person"
            rik"Just full of optimism"
            rik"Five years ago I was a decently happy and kind middle schooler"
            rik"I enjoyed cheering up my friends"
            rik"I'd always tell them it was okay"
            rik"Nine years ago, I was a loner"
            rik"No one wanted to play with me for hide and seek"
            rik"Even though I'm sad I kept it to myself"
            rik"Until the rain comes down"
            rik"I did so because no one would notice me crying"
            "You got 2000 Is-She-Kay points"
            hide r_shy with dis
            $ isk = isk + 3000
        elif (score_player < score_opponent):
            show r_happy with dis:
                xalign 0.5
                yalign 1.0
            rik"That was easy!"
            rik"Best of luck for your final showdown with Isabelle"
            mc"Sigh"
        else:
            show r with dis:
                xalign 0.5
                yalign 1.0
            rik"Not bad hihi!"
            "You got 500 Is-She-Kay points"
            $ isk = isk + 500
        $ chance = renpy.random.randint(1,10)
        # chance "passed" to free time
        hide screen score
        hide space
        jump free_time

label showdown_isabelle:
    show classroom with dis
    show i with dis:
        xalign 0.5
        yalign 1.0
    i"Hmph"
    i"This is your final showdown"
    hide i with dis
    show i_smile with dis:
        xalign 0.5
        yalign 1.0
    i"Prepare to lose"
    hide i_smile with dis
    hide classroom
    ####
    $ los = 0
    $ destiny = 0
    $ dg = 1
    show cave with dis
    "You are an adventurer in another dimension where there is no modern technology."
    "People still commute with horses, houses’ roofs are made of thatch and soldiers still fight with swords."
    "In this particular dimension, magic exists and as a result, there lived an Evil Dark Lord that wants to absorb magic
    from all living beings to make him the most powerful being in the whole universe."
    "Magic exists inside all living beings, be it plants, people, or animals. There are exceptions when an
    inanimate object has magic inside of it. These items are called “Magic Items”."
    "Since there are magic within all living beings, there are some cases where the flow of magic inside a person’s body
    flows in synergy with its host. This is how people gain their “Talent”."
    "Talent is a special perk that one possesses.
    There are perks where a person can manipulate worldly elemental according to his/her will, there are also perks that make a
    person very strong physically."
    "To become an adventurer (an occupation that completes requests from civilians as a living),
    there is only one requirement: Have a Talent."
    "Your talent is..."
    "Destiny Gambler"
    "This talent can turn a failed decision attempt into a successful one. This Talent can only be used once"
    jump stage_1_isabelle

    label stage_1_isabelle:
        "Stage 1"
        $ renpy.pause(0.5)
        "You just got your Adventurer certificate."
        "When you are on your way back after doing your first “Quest”, you decided to sit next to a river to rest for a little while."
        "Strangely, there is a note and 2 items next to you. The note says “If you are the hero foretold, choose the right relic to hold.”"
        "There seems to be a dagger made out of hardened metal with engravings on its sheathe. Very sharp. And a rugged dagger with a standard leather and wooden sheathe."
        "Being a very slick adventurer, you used your “Item Lens” to see the stats of the relics before you."
        "The Hardened Steel Dagger which is named The Light of Starmia which has a very high attack rating for a dagger."
        "The damage rating is so big that you can defeat an enormous golem or a grand dark mage with just one strike."
        "It has extra damage for unholy beings, too. The other one is named Destiny which has a normal attack compared to other iron daggers out there."
        "There is one peculiar weapon skill, though."
        "This dagger seems to have 0 percent chance to land a critical hit but, when a critical hit lands, this dagger will deal one trillion times its normal damage."
        "Which one should you pick? (Cannot use Destiny Gambler Skill in here)"
        menu:
            "Pick “The Light of Starmia”":
                $ los = 1
                jump stage_2_isabelle
            "Pick “Destiny”":
                $ destiny = 1
                jump stage_2_isabelle
    label stage_2_isabelle:
        "Stage 2"
        $ renpy.pause(0.5)
        "You arrived at the town’s guild hall."
        "Everyone is cheering because a legendary adventurer by the name of Isabelle just downed an ancient frost wyvern"
        $ score_opponent = score_opponent + 2
        mc"What, that wasn’t fair!!"
        i"That’s just her character’s perk."
        "Suddenly, a scout adventurer slams the door open and reports that a being of pure evil, The Evil Dark Lord has appeared."
        "He said that the Dark Lord wants to suck all magic from this world to become the most powerful being in the universe."
        mc"Wait, wait, wait. How the heck could he knows any of this stuff?"
        i"Wha-? I don’t know! Don’t ask questions and just enjoy the story, you party pooper!"
        i"Sigh..."
        "You asked the scout adventurer when the Dark Lord Castle is,and he said his castle is at north of this town."
        "You and Isabelle hurried to the dark castle that mysteriously appeared out of nowhere."
        "You kick open the front gate of the mysterious castle and two moving statues are blocking your path. They said that no one could enter. What should you do?"
        menu:
            "Fight them!":
                if (los == 1):
                    jump stage_2_isabelle_fight_los
                else:
                    jump stage_2_isabelle_fight_destiny
            "Tell them you are just here to take a look (and then you sneak past them).":
                if (destiny == 0):
                    jump stage_2_isabelle_look
                else:
                    "You successfully sneak past them."
                    $ score_player = score_player + 1
                    "Isabelle used Light Sword and defeated the two statues!"
                    $ score_opponent = score_opponent + 2
                    jump stage_3_isabelle

    label stage_2_isabelle_fight_los:
        $ chance = renpy.random.randint(1,total)
        if (chance > 20):
            suc"You rolled [chance] out of [total] you needed a roll greater than 20"
            "You defeated them."
            $ score_player = score_player + 1
            $ score_opponent = score_opponent + 2
            mc"What?"
            mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
            i"Shut up and play"
            jump stage_3_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 50"
            "You failed to get your “Money Maker”"
            if (isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        $ dg = 0
                        $ score_player = score_player + 1
                        $ score_opponent = score_opponent + 2
                        mc"What?"
                        mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
                        i"Shut up and play"
                        jump stage_3_isabelle
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
            elif (isk<1000 and dg == 0):
                $ score_opponent = score_opponent + 2
                jump stage_3_isabelle
            elif (isk>=1000 and dg == 0):
                menu:
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_2_isabelle_fight_los
            else:
                menu:
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_2_isabelle_fight_los
                    "Use Destiny Gambler":
                        $ dg = 0
                        $ score_player = score_player + 1
                        $ score_opponent = score_opponent + 2
                        mc"What?"
                        mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
                        i"Shut up and play"
                        jump stage_3_isabelle


    label stage_2_isabelle_fight_destiny:
        $ chance = renpy.random.randint(1,total)
        if (chance > 80):
            suc"You rolled [chance] out of [total] you needed a roll greater than 80"
            "You got lucky. They charged at you, you put your tiny dagger in front of you, then you closed your eyes.
             When you opened your eyes again, your dagger stabs the magical core that powers the statue."
            $ score_player = score_player + 1
            jump stage_3_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 80"
            "Your dagger is not powerful enough to defeat them."
            if (isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        $ dg = 0
                        $ score_player = score_player + 1
                        $ score_opponent = score_opponent + 2
                        mc"What?"
                        mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
                        i"Shut up and play"
                        jump stage_3_isabelle
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
            elif (isk<1000 and dg == 0):
                $ score_opponent = score_opponent + 2
                jump stage_3_isabelle
            elif (isk>=1000 and dg == 0):
                menu:
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_2_isabelle_fight_destiny
            else:
                menu:
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_2_isabelle_fight_destiny
                    "Use Destiny Gambler":
                        $ dg = 0
                        $ score_player = score_player + 1
                        $ score_opponent = score_opponent + 2
                        mc"What?"
                        mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
                        i"Shut up and play"
                        jump stage_2_isabelle_fight_destiny

    label stage_3_isabelle:
        "Stage 3"
        $ renpy.pause(0.5)
        "You proceed to the throne room. The Dark Lord is there sitting on his throne."
        "The Dark Lord summons a hord of gargoyles, what should you do?"

        menu:
            "Fight Them":
                if (los == 1):
                    jump stage_3_isabelle_fight_los
                else:
                    jump stage_3_isabelle_fight_destiny
            "Run straight to the Dark Lord":
                jump stage_3_isabelle_run_straight

    label stage_3_isabelle_fight_los:
        $ chance = renpy.random.randint(1,total)
        if (chance > 20):
            suc"You rolled [chance] out of [total] you needed a roll greater than 20"
            "The Light of Starmia shines bright, the gargoyles are stunned."
            $ score_player = score_player + 2
            jump stage_4_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 20"
            "When you try to unsheathe your dagger, a gargoyle bodyslams you and interrupted your attack."
            if (isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        $ dg = 0
                        $ score_player = score_player + 1
                        jump stage_4_isabelle
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
            elif (isk<1000 and dg == 0):
                jump stage_3_isabelle
            elif (isk>=1000 and dg == 0):
                menu:
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_fight_los
            else:
                menu:
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_fight_los
                    "Use Destiny Gambler":
                        $ dg = 0
                        $ score_player = score_player + 1
                        jump stage_3_isabelle_fight_los

    label stage_3_isabelle_fight_destiny:
        $ chance = renpy.random.randint(1,total)
        if (chance > 95):
            suc"You rolled [chance] out of [total] you needed a roll greater than 95"
            "It’s not an easy task to kill all those gargoyle with nothing but a
             simple dagger with 0% critical chance. You made it, though."
            $ score_player = score_player + 2
            jump stage_4_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 20"
            "You failed to defeat all of the gargoyles."
            if (isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        $ dg = 0
                        $ score_player = score_player + 1
                        jump stage_4_isabelle
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
            elif (isk<1000 and dg == 0):
                jump stage_3_isabelle
            elif (isk>=1000 and dg == 0):
                menu:
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_fight_destiny
            else:
                menu:
                    "Continue":
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_fight_destiny
                    "Use Destiny Gambler":
                        $ dg = 0
                        $ score_player = score_player + 1
                        jump stage_4_isabelle

    label stage_3_isabelle_run_straight:
        $ chance = renpy.random.randint(1,total)
        if (chance > 50):
            suc"You rolled [chance] out of [total] you needed a roll greater than 50"
            "You ran straight to the Dark Lord"
            jump stage_4_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 50"
            "When you are running straight to the Dark Lord, you tripped on a loose brick, so embarrassing."
            if(isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        jump stage_4_isabelle
                    "Continue":
                        $ score_player = score_player - 1
                        jump stage_4_isabelle
            elif(isk>=1000):
                menu:
                    "Continue":
                        $ score_player = score_player - 1
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump stage_3_isabelle_run_straight
            elif (isk<1000 and dg == 0):
                jump stage_4_isabelle
            elif (isk>=1000 and dg == 0):
                menu:
                    "Continue":
                        $ score_player = score_player - 1
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_run_straight
            else:
                menu:
                    "Continue":
                        $ score_player = score_player - 1
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_run_straight
                    "Use Destiny Gambler":
                        $ dg = 0
                        "Isabelle killed all of the gargoyles"
                        jump stage_4_isabelle

    label stage_4_isabelle:
        $ score_opponent = score_opponent + 3
        mc"WHAT? Tell me that's a joke, I'm at my limit here..."
        i"Nope, you are destined to lose HAHAHA."
        i"But don’t lose hope, there may be a way you could win."
        i"I’ve never seen this scenario before, so I don’t know what’s so special about your character."
        "Stage 4"
        $ renpy.pause(0.5)
        "The Dark Lord stood up and gathers his dark magical power into a concentrated ball on his right hand. The final battle starts."
        "Isabelle lunges forward and used her Light Sword skill, but nothing happens."
        i"Ugh... impossible"
        "What do you want to do?"
        menu:
            "Fight":
                if (los == 1):
                    jump stage_4_isabelle_los
                else:
                    jump stage_4_isabelle_destiny
    label stage_4_isabelle_los:
        "That shiny dagger sure is very powerful, but not powerful enough."
        menu:
            "Continue":
                jump isabelle_ending
            "Re-roll Cost: 999999999999":
                jump stage_4_isabelle_los

    label stage_4_isabelle_destiny:
        $ chance = renpy.random.randint(1,total)
        fail"You rolled [chance] out of [total] you needed a roll greater than 100"
        "You stabbed the Dark Lord’s chest. It’s not enough."
        if (isk<999999999999 and dg == 1):
            menu:
                "Use Destiny Gambler":
                    "You used Destiny Gambler skill. The strike you just made is a critical hit!"
                    "The Dark Lord is overwhelmed by the damage you just caused him and the Dark Lord is defeated."
                    $ dg = 0
                    $ score_player = score_player + 100
                    jump isabelle_ending
                "Continue":
                    jump isabelle_ending
        elif (isk<999999999999 and dg == 0):
            jump isabelle_ending
        elif (isk>=999999999999 and dg == 0):
            menu:
                "Continue":
                    jump isabelle_ending
                "Re-roll Cost: 999999999999":
                    jump stage_3_isabelle_fight_destiny
        else:
            menu:
                "Continue":
                    jump isabelle_ending
                "Re-roll Cost: 999999999999":
                    jump stage_3_isabelle_fight_destiny
                "Use Destiny Gambler":
                    "You used Destiny Gambler skill. The strike you just made is a critical hit!"
                    "The Dark Lord is overwhelmed by the damage you just caused him and the Dark Lord is defeated."
                    $ dg = 0
                    $ score_player = score_player + 100
                    jump isabelle_ending


    label isabelle_ending:
        hide cave with dis
        show classroom with dis
        if (score_player > score_opponent):
            jump isabelle_win
        elif (score_player <= score_opponent):
            jump isabelle_lose
        label isabelle_win:
            show i_lost with dis:
                xalign 0.1
                yalign 1.0
            i"...."
            i"I lost"
            mc"Tell me... why are you so cold?"
            hide i_lost with dis
            show i_sad with dis:
                xalign 0.4
                yalign 1.0
            i"....."
            i"Hmm"
            i"Since I was a kid I never talked to boys because I went to an all-female school"
            i"The first time I went to university... noboy would talk to me"
            i"I was seen as a cold person that was not interested with anyone"
            i"Many people wanted to befriend me when I entered university"
            i"All seemed well, but.. they got bored of me"
            i"The reason I'm cold is because I don't want people to think I'm boring"
            i"Only the Board Game Club members never get bored of me"
            mc"Well..."
            mc"I don't find you boring"
            i"You're lying"
            mc"Believe it or not you're quite interesting"
            mc"In a different way"
            i"...."
            hide i_sad with dis
            show i_lost with dis:
                xalign 0.6
                yalign 1.0
            i"Wow! No one has ever said that to me"
            i"Here take the certificate you deserve it"
            "You received the participation certificate from Isabelle!"
            i"I wished I could give you more than that.."
            mc"We could..."
            mc"You know.. after all this"
            hide i_lost with dis
            show i_smile with dis:
                xalign 0.7
                yalign 1.0
            i"Hmmph I'll think about it"
            hide i_smile with dis
            $ finalshowdown = 1
            jump endings
        label isabelle_lose:
            show i_angry with dis:
                xalign 0.5
                yalign 1.0
            i"Hmmph"
            i"That was too easy, you're pathetic"
            hide i_angry with dis
            jump endings
