
label endings:
    hide screen actions
    hide screen stats
    hide classroom2
    hide classroom
    hide tidyroom
    hide e_neutral
    hide e_neutral2
    hide e_surprise
    hide e_confuse
    hide e_shy
    hide r_neutral
    hide r_happy
    hide r_smile
    hide r_surprise
    hide r_ready
    hide i_neutral
    hide i_neutral2
    hide i_neutral3
    hide i_smile
    hide i_surprise
    if GPA == 4:
        jump perfectGPA
    elif GPA >= 3 and finalshowdown == 1:
        jump sociableScholar
    elif GPA >= 3 and finalshowdown == 0:
        jump notSociableScholar
    elif GPA < 3 and finalshowdown == 1:
        jump sociableNotScholar
    else:
        jump neither



label perfectGPA:

    "You ditched your initial plan of getting a certificate"
    "Despite this you got a perfect GPA"
    "Not bad at all!"
    jump endofgame

label notSociableScholar:
    "You maintained a respectable GPA"
    "But in the process you did not get the certifcate"
    "Oh well, hopefully companies will hire you"
    jump endofgame

label sociableScholar:
    "You passed Isabelle's test"
    "Even so you managed to also keep up with your studies"
    "Your new found experience hass gave you confidence in
    getting a job for companies"
    jump endofgame

label sociableNotScholar:
    "You were unable to maintan your GPA"
    "Despite that, you've been quite social and got a certificate"
    "You could not land the interview you wanted"
    jump endofgame

label neither:
    "You were unable to maintain your GPA"
    "Also you did not recieve your certificate"
    "You graduate feeling sad knowing you have no hope"
    jump endofgame

label endofgame:
    "This project was created for a university assignment"
    "Credits to: Liang Cai, Eugene Sebastian, and Alexandro Mikha for creating the game"
    "Special thanks to Denny Raymond for helping in creating the poster and promotional video"
    "Background Music: https://www.bensound.com"
    "Sound Effects: https://www.audioblocks.com"
    "Finish"
