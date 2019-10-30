
#########################
#Elizabeth:
#neutral
#Yalign: -0.5
#
#Isabelle:
#neutral
#Yalign: -0.5
#
#Rika:
#neutral
#Yalign: -1.25
#########################

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
        background Solid("#0000009B")
        vbox:
            spacing 10
            text "Your score: [score_player]"
            text "[opponent]'s score: [score_opponent]"


label showdown_elizabeth:
    show classroom with dis_slow
    show e_shy with dis_fast:
        xalign 0.5
        yalign e_yalign
    e"Hey..."
    e"You will be facing me"
    i"Let the game begin!"
    mc"Uh, could you please explain what Is-she-kay is?"
    i"Let me explain since I am the {b}Story Master{/b} in this {b}Scenario{/b}."
    mc"..."
    mc"I don't even understand what you're saying. What's a {b}Story Master{/b}? And a {b}Scenario{/b}?"
    show i_neutral with dis_fast:
        xalign 0.8
        yalign i_yalign
    i"*sigh* Let me explain from the beginning"
    i"So Is-she-kay is a table top RPG where I as the {b}Story Master{/b} tell a story."
    i"This story is called a {b}Scenario{/b}."
    i"You and Elizabeth are the players. As the player you have to choose an action for each stage in the {b}Scenario{/b}."
    i"But that doesn't end there. After you select an action you have to roll a random number that needs to be greater than or equal to a certain number."
    mc"Where does that certain number come from?"
    i"It comes from the {b}Scenario{/b} book."
    mc"What? That's impossible, since we can choose what we want to do that book can't possibly map every possible {b}Scenario{/b} choices."
    show classroom with vpunch
    i"*Drops book* This book weighs 10 Kilogram for a reason."
    i"Anyways, if you don't end up getting a successful roll you can re-roll by spending Is-She-Kay points."
    i"Each {b}Scenario{/b} choice you make may earn you a score."
    i"The player with the highest score will win the game."
    hide i_neutral with dis_fast
    hide e_neutral with dis_fast
    hide classroom
    ###
    $ nullguard = 0
    show city with dis_slow
    i"Ok. Let's start with the background story."
    $ renpy.pause(0.5)
    show i_neutral with dis_fast:
        xalign 0.8
        yalign i_yalign
    i"In this scenario, the players {b}(You and Elizabeth){/b} are in a modern world where monsters exist"
    i"There is an association that exists in that world to fight those monsters when they terrorize a city"
    i"The Hero Association is what they are called. You and Elizabeth are one of the heroes in this world"
    i"The monster's population is increasing quite drastically"
    i"As a result heroes such as you are present to deal with this"
    i"{b}Elizabeth{/b} is the {b}strongest hero{/b} in the Hero Association"
    i"She has the ability to one punch everything"
    i"Unfortunately {b}you{/b} are the {b}weakest hero{/b}"
    mc"How is this fair?"
    i"I don't make the scenarios you know. However..."
    i"To make up for it you have Hyper Focus to improve yourself at superhuman pace"
    i"Rumors have surfaced stating a monster overlord has been the cause
    of the monster's population increase"
    i"Many heroes have fallen trying to fight this monster"
    i"Ok. What do you want to do?"
    menu:
        "Learn high-tech computing and immerse yourself in the world of advanced
        robotics and ultra-adaptive articial intelligence":
            jump high_tech_choice

        "Decide to make yourself stronger by learning several hundred types of martial arts":
            jump martial_arts_choice

    label high_tech_choice:
        i"Looks like you paid attention"
        $ renpy.pause(0.5)
        $ total = 100
        $ chance = renpy.random.randint(1,total)
        "Rolling..."
        $ renpy.pause(0.5)
        # 50 % chance for player
        if (chance > total / 2):
            suc"You rolled [chance] out of [total] you needed a roll greater than 50"
            i"Oh wow, you actually got a good roll"
            i"You decided to learn high-tech computing and immerse yourself in the world of advanced robotics and ultra-adaptive
             artificial intelligence. You realized that this is not an easy task even if you have Hyper Focus"
            $ chance = renpy.random.randint(1,total)
            # 80 % chance for elizabeth
            if (chance > 20):
                i"Ok Elizabeth, your turn"
                e"I think I will start killing monsters"
                e"Elizabeth earns a point!"
                $ score_opponent = score_opponent + 1
            else:
                i"Ok Elizabeth, your turn"
                e"This game seems easy, I'll just gain popularity in this world"
            jump high_tech_choice_2
        else:
            fail"You rolled [chance] out of [total]"
            i"As I expected"
            i"You failed to learn high-tech computing"
            if (isk < 1000):
                $ chance = renpy.random.randint(1,total)
                if (chance > 20):
                    i"Ok Elizabeth, your turn"
                    e"I think I will start killing monsters"
                    e"Elizabeth earns a point!"
                    $ score_opponent = score_opponent + 1
                else:
                    i"Ok Elizabeth, your turn"
                    e"This game seems easy, I'll just gain popularity in this world"
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
                            i"Ok Elizabeth, your turn"
                            e"I think I will start killing monsters"
                            e"Elizabeth earns a point!"
                            $ score_opponent = score_opponent + 1
                        else:
                            i"Ok Elizabeth, your turn"
                            e"This game seems easy, I'll just gain popularity in this world"
                            jump high_tech_choice_2

    label high_tech_choice_2:
        i"Both players are planning to meet the final boss's commander"
        $ renpy.pause(0.5)
        $ chance = renpy.random.randint(1,total)
        "Rolling..."
        # 60 % chance for player
        if (chance > 60):
            suc"You rolled [chance] out of [total] you needed a roll greater than 60"
            i"Another good roll maybe you're not that useless after all"
            i"You already mastered the art of making advanced AI and you made
            an exoskeleton that you can use to amplify your weak physical strength. Bravo!"
            $ score_player = score_player + 2
            jump high_tech_choice_3
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 60"
            i"Better luck next time loser"
            i"You tried to use your skill Hyper Focus to study advanced AI and robotics. However, you are unable to
            learn it fast enough. Time is almost up, you can only make standard AI and exoskeleton to aid you in battle."
            if (isk < 1000):
                i"Ok, now its Elizabeth's turn"
                e"I'll just start killing monsters"
                i"Point to Elizabeth"
                i"Point to you as well"
                $ score_player = score_player + 1
                $ score_opponent = score_opponent + 1
                jump high_tech_choice_3
            else:
                menu:
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump high_tech_choice_2

                    "Continue":
                        $ chance = renpy.random.randint(1,total)
                        # 100 % chance for elizabeth
                        i"Ok, now its Elizabeth's turn"
                        e"I'll just start killing monsters"
                        i"Point to Elizabeth"
                        i"Point to you as well"
                        $ score_player = score_player + 1
                        $ score_opponent = score_opponent + 1
                        jump high_tech_choice_3

    label high_tech_choice_3:
        i"Both players are going to meet the final boss's commander"
        $ renpy.pause(0.5)
        $ chance = renpy.random.randint(1,total)
        "Rolling..."
        if (chance > 20 ):
            # 80 % chance for player
            suc"You rolled [chance] out of [total] you needed a roll greater than 20"
            i"You're just lucky..."
            i"You made a visor with an AI that can analyze your enemies.
             You detected what their weaknesses are and strike them with your exoskeleton."
            i"2 points to you"
            $ score_player = score_player + 2
            $ chance = renpy.random.randint(1,total)
            i"Ok Elizabeth what do you want to do?"
            e"Hmm.."
            if (chance > 20):
                # 80 % chance for elizabeth
                e"I'll go for a direct hit"
                i"Two points for Elizabeth"
                $ score_opponent = score_opponent + 2
            else:
                e"Nothing for now I guess"
                i"Elizabeth, underestimating her opponent gets thrown off the area!"
            jump high_tech_choice_4
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 20"
            i"You made a visor with an AI that can analyze your enemies. However, the enemy you are facing right
            now is very unpredictable, thus your ultra-adaptive AI couldn’t find its weaknesses. You managed to defeat it, though."
            if (isk < 1000):
                i"One point to you"
                $ score_player = score_player + 1
                jump high_tech_choice_4
            else:
                menu:
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump high_tech_choice_3

                    "Continue":
                        $ chance = renpy.random.randint(1,total)
                        i"Ok Elizabeth what do you want to do?"
                        e"Hmm.."
                        if (chance > 20):
                            # 80 % chance for elizabeth
                            e"I'll go for a direct hit"
                            i"Two points for Elizabeth"
                            $ score_opponent = score_opponent + 2
                        else:
                            e"I'll go for a direct hit"
                            i"Elizabeth, underestimating her opponent gets thrown off the area!"
                        jump high_tech_choice_4

    label high_tech_choice_4:
        i"There a small room in between the commanders’ area and the final throne room."
        i"You and Elizabeth stayed there a while, preparing for what comes next."
        $ renpy.pause(0.5)
        menu:
            "Roll":
                $ chance = renpy.random.randint(1,total)
        "Rolling..."
        if (chance > 50):
            suc"You rolled [chance] out of [total] you needed a roll greater than 50"
            i"Thinking that the final boss should have some kind of shield. You successfully made a
            hyper-adaptive device that can nullify any defensive mechanisms. You called it the Null Guard"
            i"Point to you"
            $ score_player = score_player + 1
            $ nullguard = 1
            i"Elizabeth can't do anything this turn"
            e"Ok. Pass"
            jump high_tech_choice_5
        else:
            i"Thinking that the final boss should have some kind of shield. Your adaptive
            AI can’t seem to find a critical point of modelling to make your gadget a reality."
            i"Just an advice loser, I'd use all my re-rolls here"
            if (isk<400):
                i"Elizabeth can't do anything this turn"
                e"Ok. Pass"
                jump high_tech_choice_5
            else:
                menu:
                    "Re-roll Cost: 400":
                        $ isk = isk - 400
                        jump high_tech_choice_4
                    "Continue":
                        i"Elizabeth can't do anything this turn"
                        e"Ok. Pass"
                        jump high_tech_choice_5

    label high_tech_choice_5:
        i"There is only one storyline here"
        i"This will depend entirely on whether you made Null Guard or not"
        $ renpy.pause(0.5)
        if (nullguard == 1):
            i"Since you succeeded in making the Null Guard..."
            i"You defeated the final boss"
            i"You get 3 points"
            $ score_player = score_player + 3
        else:
            i"You failed in making Null Guard"
            i"Just like you do in life"
            i"Final boss gets defeated by Elizabeth's character"
            i"3 points for her"
            $ score_opponent = score_opponent + 3
        jump elizabeth_ending

    # martial arts branch


    label martial_arts_choice:
        $ renpy.pause(0.5)
        i"You decided to make yourself stronger by learning several hundred types of martial arts."
        i"Are you even trying?"
        mc"What's wrong with my choice?"
        i"Oh, nothing"
        i"Elizabeth your turn"
        e"I think I'll just gain popularity around the world"

        jump martial_arts_choice_2

    label martial_arts_choice_2:
        i"Now both players planning on how to fight the boss's commander"
        $ renpy.pause(0.5)
        $ chance = renpy.random.randint(1,total)
        "Rolling..."
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            i"Surprisingly, the knowledge of several hundred martial arts and intense training
            made you physically competent. Your physical strength is now equal to the top heroes’ capabilities"
            i"You got really lucky"
            $ score_player = score_player + 1
            e"I'll kill monsters I guess"
            $ score_opponent = score_opponent + 1
            jump martial_arts_choice_3
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 90"
            i"As expected, no matter how much you train, you are still weak. You can kill
             some monsters, but at this rate, there is no hope for you in defeating the final boss commander."
            i"Weak just like the person playing him"
            mc"What?"
            i"Oh, nothing"
            if (isk<1000):
                i"Your turn Elizabeth"
                e"I'll kill monsters I guess"
                i"One point to Elizabeth!"
                $ score_opponent = score_opponent + 1
                jump martial_arts_choice_3
            menu:
                "Re-roll Cost: 1000":
                    $ isk = isk - 1000
                    jump martial_arts_choice_2

                "Continue":
                    # 100 % chance for elizabeth
                    i"Your turn Elizabeth"
                    e"I'll kill monsters I guess"
                    i"One point to Elizabeth!"
                    $ score_opponent = score_opponent + 1
                    jump martial_arts_choice_3

    label martial_arts_choice_3:
        i"Now both players are meeting the boss's commander"
        $ renpy.pause(0.5)
        menu:
            "Roll":
                $ chance = renpy.random.randint(1,total)
        "Rolling..."
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            i"You successfully executed the sacred Dragon Waterfall Strike technique on one of the commanders."
            i"Interesting..."
            jump martial_arts_choice_4
        else:
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            i"You have failed to execute the sacred Dragon Waterfall Strike technique on one of the commanders"
            i"As expected"
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
                            i"Your turn Elizabeth"
                            e"I'll start punching the commander"
                            i"One Punched"
                            i"2 points awarded to Elizabeth!"
                            $ score_opponent = score_opponent + 2
                            i"One point to you... for trying I guess?"
                            $ score_player = score_player + 1
                        else:
                            i"Your turn Elizabeth"
                            e"I'll start punching the commander"
                            i"Elizabeth gets knocked out due to underestimating her opponent"
                            i"One point to you... for trying I guess?"
                            $ score_player = score_player + 1
                        jump martial_arts_choice_4
    label martial_arts_choice_4:
        i"There a small room in between the commanders’ area and the final throne room."
        i"You and Elizabeth stayed there a while, preparing for what comes next."
        $ renpy.pause(0.5)
        $ chance = renpy.random.randint(1,total)
        if (chance > 75):
            suc"You rolled [chance] out of [total] you needed a roll greater than 75"
            i"You feel enlightened and your strength has increased tenfold"
            i"Point to you"
            $ score_player = score_player + 1
            jump martial_arts_choice_5
        else:
            i"You don’t feel anything special"
            i"Just like you"
            mc"I heard that"
            if (isk<1000):
                jump martial_arts_choice_5
            else:
                menu:
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump martial_arts_choice_5
                    "Continue":
                        i"Since there isn’t anything Elizabeth can do to improve herself,
                         she can only pass her turn."
                        jump martial_arts_choice_4

    label martial_arts_choice_5:
        i"There is only one storyline here"
        i"It will depend upon whether you can use the Ultimate Sky-Dragon Judgement Move"
        $ renpy.pause(0.5)
        $ chance = renpy.random.randint(1,total)
        if (chance > 95):
            i"..."
            i"I'm speechless"
            suc"You rolled [chance] out of [total] you needed a roll greater than 95"
            i"*sigh*"
            i"You defeated the boss using the Ultimate Sky-Dragon Judgement move"
            i"3 points to you"
            $ score_player = score_player + 3
            $ chance = renpy.random.randint(1,10)
            # chance "passed" to free time
            hide screen score
            jump free_time
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 95"
            i"You failed to defeat the boss"
            i"What did you expect it was 5 percent chance of succeeding"
            if (isk<1000):
                i"Since your character is deadweight Elizabeth proceeds to defeat the boss"
                i"3 points to Elizabeth"
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
        hide screen score with dis_slow
        hide city with dis_slow
        show classroom with dis_slow
        i"The final score of the player is [score_player]"
        i"And Elizabeth's score is [score_opponent]"
        if (score_player > score_opponent):
            i"Therefore the player wins"
            i"Looks like you aren't so bad after all"
            e"Good game, well played..."
            rika"You're going to be facing me in the next showdown"
            rika"I warn ya it ain't gonna be easy"
            "You gained 2000 Is-She-Kay points for winning"
            $ isk = isk + 2000
            "You unlocked Elizabeth's past"
            "Would you like to check it?"
            menu:
                "Yes":
                    "There was a young girl. Her eyes are not perfect so she wears a thick pair of glasses whenever she goes to school."
                    "She also likes reading comics and collecting them, too. When she was in fifth grade, her friends make fun of her because she wears glasses and her twin ponytails."
                    "They called her a nerd because she loves to read comic books. This goes on until she was in middle school."
                    "When she was in high school, she completely changed her appearance even though she feels uncomfortable doing it. That is why she often overthinks how she looks in public."
                    "She doesn't even want people to know that she likes to read manga. She replaced her thick glasses with a pair of contact lenses and start living as another person when she is in public."
                "Continue":
                    jump free_time
        elif (score_player < score_opponent):
            i"Heh.. as expected the loser loses"
            e"Well he just started playing"
            i"That's a lame excuse"
            i"If you can't play you might as well just focus on studying"
            i"I sure hope you're not crying"
            mc"I'm not..."
            mc"It's the onions, it's so strong"
            rika"Oops hihi I was wondering where my food went"
            jump free_time
        else:
            e"Well for this showdown it's declared as a draw"
            e"Well played"
            i"But you won't get lucky"
            i"Because in the rulebook if you face me and you draw you lose"
            mc"What kind of rule is th-"
            i"Club's rules, now shut up before I kick you out"
            mc"*sigh*"
            "You gained 500 Is-She-Kay points for winning"
            $ isk = isk + 500
            jump free_time
label showdown_rika:
    show classroom with dis_slow
    show r_neutral with dis_fast:
        xalign 0.5
        yalign r_yalign
    rik"Hiya!"
    rik"It's time to face me!"
    i"In this showdown both me and Elizabeth will be the story master"

    hide classroom
    ####
    $ minor_injury = 0
    $ no_fuel = 0
    $ damaged_ship = 0
    $ score_opponent = 0
    show space with dis_slow
    i"This encounter is slightly different in decision making"
    i"Instead of generating a random number to determine good decision"
    i"You can choose what to do but it's not 100 percent success"
    i"Keep in mind that if you choose a bad decision the odds of you winning the game will be slim"
    i"Now I'll get to the background story"
    $ renpy.pause(0.5)
    i"You are a merchant, travelling through the ever expanding space to make a living"
    i"One day, you heard a rumor about a kind of mysterious device that can make money out of nothing"
    i"As a merchant, your ears stood up and you immediately begin your journey to get that device"
    i"You are not alone, however"
    i"There are other merchants that want to gain possession of that device as well"
    i"You are at a space bar"
    mc"Uh? You mean the keyboard button in my computer?"
    i"*sigh* Aren't you supposed to be one of the smartest in your class?"
    i"You just heard the rumor about the “Money Maker”, a device that can make money out of thin air"
    i"You decided to go through the door. Another muscular merchant pushed you away from the"
    i"door when you are trying to get outside. What are you going to do about this situation?"
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
        mc"Wait where is rika?"
        i"Rika has her seperate scenario. To make it interesting her score will be revealed in the end"
        $ renpy.pause(0.5)
        i"You got out from the bar"
        i"Time is short, you can either fix the small shallow hole on the side of your ship or you can refuel your ship"
        i"Remember, your ship is a futuristic, super high tech vehicle"
        menu:
            "Refuel":
                $ damaged_ship = 1
                jump stage_3_rika
            "Fix the shallow hole":
                $ no_fuel = 1
                jump stage_3_rika
    label stage_3_rika:
        $ renpy.pause(0.5)
        i"You are done preparing for a long journey, you set sail to the “Money Maker”"
        i"Rumor has it that the money maker is located at the “Ramvizian System”, 10 light years away from you at the moment"
        i"You can either: Enter a wormhole (rather unstable) or initiate Hyperspeed drive (stable, but time and resource consuming)"
        i"I'm pretty sure you have a bit of common sense with the choice you make"
        menu:
            "Enter a wormhole":
                if (damaged_ship == 1):
                    i"You have defied my expectations"
                    jump stage_3_rika_damaged_ship
                else:
                    suc"Got through the wormhole safely"
                    $ score_player = score_player + 2
                    jump stage_4_rika

            "Initiate Hyperspeed drive":
                if (no_fuel == 1):
                    i"Seriously what do you learn in school?"
                    jump stage_3_rika_no_fuel
                else:
                    suc"You had enough fuel to get to your destination"
                    $ score_player = score_player + 1

    label stage_3_rika_damaged_ship:
        $ chance = renpy.random.randint(1,total)
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            i"Got through the wormhole safely"
            i"Luck wins when common sense fails"
            i"2 points to you"
            $ score_player = score_player + 2
            jump stage_4_rika
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 90"
            i"Your ship can’t handle the harsh nature of the wormhole"
            if(isk<1000):
                i"You lose two points"
                $ score_player = score_player - 2
                jump stage_4_rika
            else:
                menu:
                    "Continue":
                      i"You lose two points"
                      $ score_player = score_player - 2
                      jump stage_4_rika
                    "Re-roll Cost: 1000":
                        $ isk = isk - 1000
                        jump stage_3_rika_damaged_ship

    label stage_3_rika_no_fuel:
        $ chance = renpy.random.randint(1,total)
        if (chance > 90):
            suc"You rolled [chance] out of [total] you needed a roll greater than 90"
            i"You had just enough fuel to get to your destination"
            i"Common sense is really not that common is it"
            i"One point to you"
            $ score_player = score_player + 1
            jump stage_4_rika
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 90"
            i"Your ship can’t handle the harsh nature of the wormhole"
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
        $ renpy.pause(0.5)
        i"You landed on the planet where the “Money Maker” resides. Everyone is shooting one another in front of it"
        i"You have your trusty Laser Blaster with you"
        i"You can blast your way past them all to get the “Money Maker” or you can go the sneaky beaky way."
        i"What's your move?"
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
            i"You blast everyone that goes in your way and get your hand on the “Money Maker”"
            i"2 points to the player"
            $ score_player = score_player + 2
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 90"
            i"Ouch! The Injury from the bar fight has gone worse. You can’t go any further"
            i"I mean you're injured-"
            mc"Yes I know what you're gonna say I messed up"
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
        if (chance > 10):
            suc"You rolled [chance] out of [total] you needed a roll greater than 10"
            i"You blast everyone that goes in your way and get your hand on the “Money Maker”"
            i"2 points to you"
            $ score_player = score_player + 2
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 10"
            i"Your ammunition runs out, you proceed to sneak past them all"
            mc"Failed but not really huh?"
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
        $ renpy.pause(0.5)
        i"You are a finger away on getting your hands on the “Money Maker”"
        i"However, your lifetime rival, Rika is there too! You have no choice but to fight her"
        rika"Why hello there"
        i"You can either fight or fight"
        mc"Uh? What? What's the difference?"
        i"Shut up it's in the book unless you want me to slam the book to your face"
        mc"*sigh* fine..."
        $ score_opponent = renpy.random.randint(9,10)
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
        i"Elizabeth take it from here"
        e"Yes..."
        if (chance > 95):
            suc"You rolled [chance] out of [total] you needed a roll greater than 95"
            e"Despite your injuries, you relentlessly fought for your own “Money Maker”"
            e"3 points to the player"
            $ score_player = score_player + 3
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 95"
            e"Your Injuries has failed you"
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
        i"Elizabeth take it from here"
        e"Yes..."
        if (chance > 50):
            suc"You rolled [chance] out of [total] you needed a roll greater than 50"
            e"Despite your injuries, you relentlessly fought for your own “Money Maker”."
            e"Oh that's great!"
            e"3 points to the player"
            $ score_player = score_player + 3
            jump rika_ending
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 50"
            e"You failed to get your “Money Maker”"
            e"Oh no..."
            if(isk<400):
                jump rika_ending
            else:
                menu:
                    "Continue":
                        jump rika_ending
                    "Re-roll Cost: 400":
                        jump stage_5_rika_no_injury



    label rika_ending:
        show screen classroom with dis_slow
        e"The final score of the player is [score_player]"
        e"And Elizabeth's score is [score_opponent]"
        if (score_player>score_opponent):
            e"You win"
            rika"Not bad I guess"
            "You got 3000 Is-She-Kay points"
            $ isk = isk + 3000
            "Rika's story unlocked"
            "Would you like to open it?"
            menu:
                "Yes":
                    "Two years ago she was a very cheerful high schooler. She smiled all the time. She sees everything from a positive point of view."
                    "Five years ago, she was a decently happy and kind  middle schooler. She likes to cheer up her friends when in need and tell them that it was all okay."
                    "Nine Years ago, she was a lonely little girl that no one likes. She is left alone playing at the park when the whole class played hide and seek at recess."
                    "Even though she is sad, she held back her tears until the rain comes down. She held back because she knows under the rain, nobody would notice her crying."
                    $ chance = renpy.random.randint(1,10)
                    # chance "passed" to free time
                    hide screen score
                    hide space
                    jump free_time
                "Continue":
                    $ chance = renpy.random.randint(1,10)
                    # chance "passed" to free time
                    hide screen score
                    hide space
                    jump free_time
        elif (score_player < score_opponent):
            e"You..."
            e"Lose"
            show r_happy with dis_fast:
                xalign 0.5
                yalign r_yalign
            rika"That was easy!"
            rika"Do better next time"
            mc"*sigh* Guess I have to..."
        else:
            e"It's a draw"
            show r with dis_fast:
                xalign 0.5
                yalign r_yalign
            rika"Not bad hihi!"
            mc"That was close"
            rika"Yeah, unfortunately no rematch"
            rika"Best of luck with Isabelle!"
            "You got 750 Is-She-Kay points"
            $ isk = isk + 750
        $ chance = renpy.random.randint(1,10)
        # chance "passed" to free time
        hide screen score
        hide space
        jump free_time

label showdown_isabelle:
    show classroom with dis_slow
    show i_neutral with dis_fast:
        xalign 0.5
        yalign i_yalign
    i"Hmph"
    i"This is your final showdown"

    hide i_neutral with dis_fast
    show i_smile with dis_fast:
        xalign 0.5
        yalign i_yalign
    i"Prepare to lose"
    hide i_smile with dis_fast
    hide classroom
    ####
    $ los = 0
    $ destiny = 0
    $ dg = 1
    show cave with dis_slow
    rika"In this case..."
    e"..."
    rika"Elizabeth?"
    e"Oh right.. both of us will be the story master"
    rika"There is an interesting mechanic here that-"
    e"allows you as the player to use your character's Talent"
    rika"You are an adventurer in another dimension where there is no modern technology"
    e"People still commute with horses, houses’ roofs are made of thatch and soldiers still fight with swords."
    rika"In this particular dimension, magic exists and as a result, there lived an Evil Dark Lord that wants to absorb magic"
    e"from all living beings to make him the most powerful being in the whole universe."
    rika"Magic exists inside all living beings, be it plants, people, or animals. There are exceptions when an-"
    e"inanimate object has magic inside of it. These items are called “Magic Items”."
    rika"Since there are magic within all living beings, there are some cases where the flow of magic inside a person’s body-"
    e"flows in synergy with its host. This is how people gain their “Talent”."
    rika"Talent is a special perk that one possesses."
    e"There are perks where a person can manipulate worldly elemental according to his/her will,-"
    rika"there are also perks that make a person very strong physically."
    e"To become an adventurer (an occupation that completes requests from civilians as a living),-"
    rika"there is only one requirement: Have a Talent."
    e"Your talent is..."
    rika"Destiny Gambler"
    e"This talent can turn a failed decision attempt into a successful one. This Talent can only be used once"
    rika"Wew that was perfect Elizabeth we spent days practicing this narration"
    e"I guess so..."
    jump stage_1_isabelle

    label stage_1_isabelle:
        $ renpy.pause(0.5)
        rika"You just got your Adventurer certificate."
        e"When you are on your way back after doing your first “Quest”, you decided to sit next to a river to rest for a little while."
        rika"Strangely, there is a note and 2 items next to you. The note says “If you are the hero foretold, choose the right relic to hold.”"
        e"There seems to be a dagger made out of hardened metal with engravings on its sheathe. Very sharp. And a rugged dagger with a standard leather and wooden sheathe."
        rika"Being a very slick adventurer, you used your “Item Lens” to see the stats of the relics before you."
        e"The Hardened Steel Dagger which is named The Light of Starmia which has a very high attack rating for a dagger."
        rika"The damage rating is so big that you can defeat an enormous golem or a grand dark mage with just one strike."
        e"It has extra damage for unholy beings, too. The other one is named Destiny which has a normal attack compared to other iron daggers out there."
        rika"There is one peculiar weapon skill, though."
        e"This dagger seems to have 0 percent chance to land a critical hit but, when a critical hit lands, this dagger will deal one trillion times its normal damage."
        rika"Which one should you pick? (Cannot use Destiny Gambler Skill in here)"
        rika"If you're having difficulties..."
        rika"Would you rather date me or Elizabeth?"
        mc"What?"
        e"*blushes*"
        menu:
            "Pick “The Light of Starmia”":
                $ los = 1
                jump stage_2_isabelle
            "Pick “Destiny”":
                $ destiny = 1
                jump stage_2_isabelle
    label stage_2_isabelle:
        $ renpy.pause(0.5)
        e"You arrived at the town’s guild hall."
        rika"Everyone is cheering because a legendary adventurer by the name of Isabelle just downed an ancient frost wyvern"
        $ score_opponent = score_opponent + 2
        mc"What, that wasn’t fair!!"
        i"That’s just her character’s perk."
        e"Suddenly, a scout adventurer slams the door open and reports that a being of pure evil, The Evil Dark Lord has appeared."
        rika"He said that the Dark Lord wants to suck all magic from this world to become the most powerful being in the universe."
        mc"Wait, wait, wait. How the heck could he knows any of this stuff?"
        i"Wha-? I don’t know! Don’t ask questions and just enjoy the story, you party pooper!"
        mc"Sigh..."
        e"You asked the scout adventurer when the Dark Lord Castle is,and he said his castle is at north of this town."
        rika"You and Isabelle hurried to the dark castle that mysteriously appeared out of nowhere."
        e"You kick open the front gate of the mysterious castle and two moving statues are blocking your path. They said that no one could enter. What should you do?"
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
                    e"1 point to the player"
                    $ score_player = score_player + 1
                    "Isabelle used Light Sword and defeated the two statues!"
                    e"2 points to isabelle"
                    $ score_opponent = score_opponent + 2
                    jump stage_3_isabelle

    label stage_2_isabelle_fight_los:
        $ chance = renpy.random.randint(1,total)
        rika"You know all this talking is making me hungry I'm going to grab a quick snack be right back!"
        e"Eh? But..."
        if (chance > 20):
            suc"You rolled [chance] out of [total] you needed a roll greater than 20"
            e"Uh?.. You defeated them."
            e"1 Point for the player"
            $ score_player = score_player + 1
            e"Isabelle kills the remaining statue and gets 2 points!"
            $ score_opponent = score_opponent + 2
            mc"What?"
            mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
            e"It says it right here in the book-"
            mc"Let me see"
            mc"That was written in pencil I ca-"
            i"Shut up and play"
            mc"*sigh*"
            jump stage_3_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 20"
            e"You failed to get your “Money Maker”"
            mc"What?"
            e"Oh! I mean you failed to defeat them"
            if (isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        $ dg = 0
                        e"One Point for the player"
                        $ score_player = score_player + 1
                        e"Isabelle kills the remaining statue and gets 2 points!"
                        $ score_opponent = score_opponent + 2
                        mc"What?"
                        mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
                        e"It says it right here in the book-"
                        mc"Let me see"
                        mc"That was written in pencil I ca-"
                        i"Shut up and play"
                        mc"*sigh*"
                        jump stage_3_isabelle
                    "Continue":
                        e"Isabelle kills both statues and gets 2 points!"
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
            elif (isk<1000 and dg == 0):
                e"Isabelle kills both statues and gets 2 points!"
                $ score_opponent = score_opponent + 2
                jump stage_3_isabelle
            elif (isk>=1000 and dg == 0):
                menu:
                    "Continue":
                        e"Isabelle kills both statues and gets 2 points!"
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_2_isabelle_fight_los
            else:
                menu:
                    "Continue":
                        e"Isabelle kills both statues and gets 2 points!"
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_2_isabelle_fight_los
                    "Use Destiny Gambler":
                        $ dg = 0
                        e"One Point for the player"
                        $ score_player = score_player + 1
                        e"Isabelle kills the remaining statue and gets 2 points!"
                        $ score_opponent = score_opponent + 2
                        mc"What?"
                        mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
                        e"It says it right here in the book-"
                        mc"Let me see"
                        mc"That was written in pencil I ca-"
                        i"Shut up and play"
                        jump stage_3_isabelle


    label stage_2_isabelle_fight_destiny:
        $ chance = renpy.random.randint(1,total)
        if (chance > 80):
            suc"You rolled [chance] out of [total] you needed a roll greater than 80"
            e"You got lucky. They charged at you, you put your tiny dagger in front of you, then you closed your eyes"
            e"When you opened your eyes again, your dagger stabs the magical core that powers the statue."
            e"One point to the player!"
            $ score_player = score_player + 1
            e"Isabelle kills the remaining statue and gets 2 points!"
            $ score_opponent = score_opponent + 2
            mc"What?"
            mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
            e"It says it right here in the book-"
            mc"Let me see"
            mc"That was written in pencil I ca-"
            jump stage_3_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 80"
            e"Your dagger is not powerful enough to defeat them"
            if (isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        $ dg = 0
                        e"1 point to the player!"
                        $ score_player = score_player + 1
                        e"Isabelle kills the remaining statue and gets 2 points!"
                        $ score_opponent = score_opponent + 2
                        mc"What?"
                        mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
                        e"It says it right here in the book-"
                        mc"Let me see"
                        mc"That was written in pencil I ca-"
                        i"Shut up and play"
                        jump stage_3_isabelle
                    "Continue":
                        e"Isabelle kills both statues and gets 2 points!"
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
            elif (isk<1000 and dg == 0):
                e"Isabelle kills both statues and gets 2 points!"
                $ score_opponent = score_opponent + 2
                jump stage_3_isabelle
            elif (isk>=1000 and dg == 0):
                menu:
                    "Continue":
                        e"Isabelle kills both statues and gets 2 points!"
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
                        e"1 point to the player"
                        $ score_player = score_player + 1
                        e"And 2 points to Isabelle"
                        $ score_opponent = score_opponent + 2
                        mc"What?"
                        mc"She got 2 score for defeating one statue and I got one? That’s cheating!"
                        e"It says it right here in the book-"
                        mc"Let me see"
                        mc"That was written in pencil I ca-"
                        i"Shut up and play"
                        mc"*sigh*"
                        jump stage_2_isabelle_fight_destiny

    label stage_3_isabelle:
        $ renpy.pause(0.5)
        rika"Hey Elizabeth I'm back, oh let me do this one!"
        e"Uh... sure"
        rika"You proceed to the throne room. The Dark Lord is there sitting on his throne."
        rika"The Dark Lord summons a hord of gargoyles, what should you do?"

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
            rika"The Light of Starmia shines bright, the gargoyles are stunned."
            rika"2 points to the player!"
            $ score_player = score_player + 2
            jump stage_4_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 20"
            rika"When you try to unsheathe your dagger, a gargoyle bodyslams you and interrupted your attack."
            if (isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        $ dg = 0
                        rika"1 point to the player!"
                        $ score_player = score_player + 1
                        jump stage_4_isabelle
                    "Continue":
                        rika"2 points to Isabelle!"
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
            elif (isk<1000 and dg == 0):
                jump stage_3_isabelle
            elif (isk>=1000 and dg == 0):
                menu:
                    "Continue":
                        rika"2 points to Isabelle!"
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_fight_los
            else:
                menu:
                    "Continue":
                        rika"2 points to Isabelle!"
                        $ score_opponent = score_opponent + 2
                        jump stage_3_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_fight_los
                    "Use Destiny Gambler":
                        $ dg = 0
                        rika"1 point to the player!"
                        $ score_player = score_player + 1
                        jump stage_3_isabelle_fight_los

    label stage_3_isabelle_fight_destiny:
        $ chance = renpy.random.randint(1,total)
        if (chance > 95):
            suc"You rolled [chance] out of [total] you needed a roll greater than 95"
            rika"It’s not an easy task to kill all those gargoyle with nothing but a
             simple dagger with 0% critical chance. You made it, though."
            rika"Well that was hilarious"
            rika"2 points to the player!"
            $ score_player = score_player + 2
            jump stage_4_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 20"
            rika"You failed to defeat all of the gargoyles."
            if (isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        $ dg = 0
                        rika"1 point to the player!"
                        $ score_player = score_player + 1
                        jump stage_4_isabelle
                    "Continue":
                        i"2 points to me"
                        rika"2 points to Isabelle!"
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
            elif (isk<1000 and dg == 0):
                rika"2 points to Isabelle!"
                $ score_opponent = score_opponent + 2
                jump stage_3_isabelle
            elif (isk>=1000 and dg == 0):
                menu:
                    "Continue":
                        rika"2 points to Isabelle!"
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_fight_destiny
            else:
                menu:
                    "Continue":
                        rika"2 points to Isabelle!"
                        $ score_opponent = score_opponent + 2
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_fight_destiny
                    "Use Destiny Gambler":
                        $ dg = 0
                        rika"1 point to the player!"
                        $ score_player = score_player + 1
                        jump stage_4_isabelle

    label stage_3_isabelle_run_straight:
        $ chance = renpy.random.randint(1,total)
        if (chance > 50):
            suc"You rolled [chance] out of [total] you needed a roll greater than 50"
            rika"You ran straight to the Dark Lord"
            jump stage_4_isabelle
        else:
            fail"You rolled [chance] out of [total] you needed a roll greater than 50"
            rika"When you are running straight to the Dark Lord, you tripped on a loose brick, so embarrassing."
            rika"That's funny!"
            e"Yeah..."
            if(isk<1000 and dg == 1):
                menu:
                    "Use Destiny Gambler":
                        jump stage_4_isabelle
                    "Continue":
                        rika"Point deducted to the player!"
                        $ score_player = score_player - 1
                        jump stage_4_isabelle
            elif(isk>=1000):
                menu:
                    "Continue":
                        rika"Point deducted to the player!"
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
                        rika"Point deducted to the player!"
                        $ score_player = score_player - 1
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_run_straight
            else:
                menu:
                    "Continue":
                        rika"Point deducted to the player!"
                        $ score_player = score_player - 1
                        jump stage_4_isabelle
                    "Re-roll Cost: 1000":
                        jump stage_3_isabelle_run_straight
                    "Use Destiny Gambler":
                        $ dg = 0
                        rika"Isabelle killed all of the gargoyles"
                        jump stage_4_isabelle

    label stage_4_isabelle:
        rika"3 points to Isabelle"
        $ score_opponent = score_opponent + 3
        mc"WHAT? Tell me that's a joke, I'm at my limit here..."
        i"Nope, you are destined to lose HAHAHA."
        i"But don’t lose hope, there may be a way you could win."
        i"I’ve never seen this scenario before, so I don’t know what’s so special about your character."
        rika"This looks interesting"
        e"So far no one has been able to beat Isabelle..."
        i"And it would stay the same"
        $ renpy.pause(0.5)
        e"The Dark Lord stood up and gathers his dark magical power into a concentrated ball on his right hand. The final battle starts."
        rika"Isabelle lunges forward and used her Light Sword skill, but nothing happens."
        i"Ugh... impossible"
        rika"Hmm.. how do you even win this scenario?"
        e"Yeah.. all probabilities have 0 chance"
        rika"And even then the rerolls are insane 999999999999 points for one?"
        rika"Anyways, what do you want to do?"
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
        e"You stabbed the Dark Lord’s chest. It’s not enough."
        rika"The Dark Lord is far too powerful..."
        if (isk<999999999999 and dg == 1):
            menu:
                "Use Destiny Gambler":
                    mc"You forgot something"
                    mc"I use my trump card!"
                    mc"Destiny Gambler!"
                    e"Ofcourse, despite how useless the character is he was given that skill"
                    rika"You used Destiny Gambler skill. The strike you just made is a critical hit!"
                    rika"The Dark Lord is overwhelmed by the damage you just caused him and the Dark Lord is defeated."
                    $ dg = 0
                    rika"100 points to the player"
                    $ score_player = score_player + 100
                    rika"No way..."
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
                    mc"You forgot something"
                    mc"I use my trump card!"
                    mc"Destiny Gambler!"
                    e"Ofcourse, despite how useless the character is he was given that skill"
                    rika"You used Destiny Gambler skill. The strike you just made is a critical hit!"
                    rika"The Dark Lord is overwhelmed by the damage you just caused him and the Dark Lord is defeated."
                    rika"You used Destiny Gambler skill. The strike you just made is a critical hit!"
                    rika"The Dark Lord is overwhelmed by the damage you just caused him and the Dark Lord is defeated."
                    $ dg = 0
                    rika"100 points to the player"
                    $ score_player = score_player + 100
                    rika"No way..."
                    jump isabelle_ending


    label isabelle_ending:
        hide cave with dis_slow
        show classroom with dis_slow
        if (score_player > score_opponent):
            jump isabelle_win
        elif (score_player <= score_opponent):
            jump isabelle_lose
        label isabelle_win:
            show i_surprise with dis_fast:
                xalign 0.1
                yalign i_yalign
            i"...."
            i"I lost"
            i"Impossible..."
            i"I can't believe it..."
            i"I almost didn't print the certificate believing I'd win"
            i"Here take it you...."
            i"Deserve it"
            "Received the certifacate from Isabelle!"
            $ finalshowdown = 1
            "Isabelle's past unlocked"
            "Would you like to view it?"
            menu:
                "Yes":
                    "From when she was little, she never talk to boys because she went to an all-female school."
                    "The first time she went to university, nobody would talk to her."
                    "She was seen as this ‘cold’ person that has no desire to talk to anyone."
                    "Many people want to be friends with her when she just entered university."
                    "All seems well, but like everyone else in her life, they eventually got bored of her."
                    "The truth behind this ‘cold’ facade that is not because she does not like those around her,"
                    "she just doesn’t want everybody to know that she is a boring individual. That is why she likes to keep things short and straightforward."
                    "The members from the Board Game Club are the only ones that never got bored of her."
                    jump endings
                "Continue":
                    jump endings
        label isabelle_lose:
            show i_thinking with dis_fast:
                xalign 0.5
                yalign i_yalign
            i"Hmmph"
            i"That was too easy"
            i"Luckily I saved paper"
            i"I knew you couldn't win so I didn't print the certificate"
            jump endings
