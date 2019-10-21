
label endings:
    hide actions
    hide stats
    hide classroom2
    hide classroom
    hide tidyroom
    if GPA == 4:
        jump perfectGPA
    elif GPA >= 3 and finalshowdown == 1:
        jump sociableScholar
    elif GPA >= 3 and finalshowdown == 0:
        jump notSociableScholarc
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
    "Fin"
