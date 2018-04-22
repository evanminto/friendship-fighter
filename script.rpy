# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define announcer = Character("Announcer")
define max_character = Character("Max")
define coach = Character("Coach")
define inferno = Character("Hurik")
define thought = Character(None, what_italic=True, what_alt="Max, thinking, [text]")

default round = 1

default player_health = 100
default opponent_health = 100
default friendship = 0

default wins = 0
default losses = 0

default round_end = False
default match_end = False
default won_match = False

default won_round_1 = False
default won_round_2 = False

default min_friendship = 75
default combo = 0
default max_combo = 0

default player_strike_dmg = 10
default player_block_dmg = 0
default player_throw_dmg = 20
default opponent_strike_dmg = 20
default opponent_block_dmg = 0
default opponent_throw_dmg = 30

image goggles_img = im.FactorScale("goggles.png", 0.1275, xalign=0.125, yalign=1.0, alt="Goggles standing in a fighting position. He has wiry hair and is wearing sports goggles.")
image goggles_energy_img = im.FactorScale("goggles energy.png", 0.1275, xalign=0.125, yalign=1.0, alt="Goggles standing in a fighting position with glowing balls of energy on his hands")
image inferno_img = im.FactorScale("inferno.png", 0.14, xalign=0.925, yalign=1.0, alt="The Inferno standing in a fighting position. He is muscular and bald, with a large scar on his cheek.")
image inferno_fire_img = im.FactorScale("inferno fire.png", 0.14, xalign=0.925, yalign=1.0, alt="The Inferno standing in a fighting position. His arms are on fire and he has hair made out of fire")

image healthbar_left_img = im.FactorScale("healthbar left.png", 0.3, xalign=0.125, yalign=0.05)
image healthbar_unit_1_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125 - 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_2_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125, yalign=0.05 + 0.006667)
image healthbar_unit_3_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125 + 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_4_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125 + 2 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_5_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125 + 3 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_6_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125 + 4 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_7_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125 + 5 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_8_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125 + 6 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_9_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125 + 7 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_10_left_img = im.FactorScale("healthbar unit left.png", 0.3, xalign=0.125 + 8 * 0.03625, yalign=0.05 + 0.006667)

image healthbar_right_img = im.FactorScale("healthbar right.png", 0.3, xalign=0.875, yalign=0.05)
image healthbar_unit_1_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875 + 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_2_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875, yalign=0.05 + 0.006667)
image healthbar_unit_3_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875 - 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_4_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875 - 2 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_5_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875 - 3 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_6_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875 - 4 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_7_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875 - 5 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_8_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875 - 6 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_9_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875 - 7 * 0.03625, yalign=0.05 + 0.006667)
image healthbar_unit_10_right_img = im.FactorScale("healthbar unit right.png", 0.3, xalign=0.875 - 8 * 0.03625, yalign=0.05 + 0.006667)

image infinity_img = im.FactorScale("infinity.png", 0.3, xalign=0.5, yalign=0.055)

image player_health_text = renpy.ParameterizedText()
image opponent_health_text = renpy.ParameterizedText()
image combo_text = renpy.ParameterizedText(xalign=0.09, yalign=0.25, size=40, font="fonts/PermanentMarker-Regular.ttf")
image friendship_text = renpy.ParameterizedText()

label update_friendship:
    python:
        friendship += max_combo * 5
        friendship = min(max(0, friendship), 100)

    return

label start:
    show background

    coach "Alright Max, this is it, your big debut fight! How are you feeling?"

    max_character "I-I'm not sure I can do this. I just barely made it out of my last fight. I don't stand a chance against this {b}\"Inferno\"{/b} guy!"

    coach "You'll be alright as long as you stick to your training. Remember, every turn you can choose to either {b}STRIKE{/b}, {b}BLOCK{/b}, or {b}THROW{/b}."
    coach "But Inferno will be choosing his own moves every turn too. You need to pick the right one to beat his move."
    coach "{b}BLOCKS stop STRIKES{/b}, {b}STRIKES interrupt THROWS{/b}, and {b}THROWS break BLOCKS{/b}. It's just like—"

    max_character "Yeah yeah, like {b}rock paper scissors{/b}. But he's so strong, if he lands even a few moves on me I'm done for!"

    coach "Lucky for you, Inferno is a creature of habit. If you {b}learn his patterns{/b} you can predict his next move and choose the right move to beat him."

    max_character "I sure hope this works..."

    coach "Oh, one more thing! Winning the match is all well and good, but you know what's more valuable than any trophy?"

    max_character "Not this again..."

    coach "That's right! {b}Friendship!{/b}"
    coach "Inferno respects strong fighters, so you'll want to land {b}combos{/b} to show him how strong you are."
    coach "To land a combo, just {b}hit him a bunch of times without getting hit yourself{/b}. Once you get hit you're back to zero!"
    coach "If you can beat Inferno {b}and{/b} gain his respect, you'll have won more than just the match."

    jump round1_start

label update_status:
    python:
        player_health = min([max([player_health, 0]), 100])
        opponent_health = min([max([opponent_health, 0]), 100])
        friendship = min([max([friendship, 0]), 100])
        status = "Player: " + str(player_health) + ", Opponent: " + str(opponent_health) + ", Friendship: " + str(friendship)

    if not match_end:
        hide healthbar_unit_1_left_img
        hide healthbar_unit_2_left_img
        hide healthbar_unit_3_left_img
        hide healthbar_unit_4_left_img
        hide healthbar_unit_5_left_img
        hide healthbar_unit_6_left_img
        hide healthbar_unit_7_left_img
        hide healthbar_unit_8_left_img
        hide healthbar_unit_9_left_img
        hide healthbar_unit_10_left_img

        if player_health >= 10:
            show healthbar_unit_1_left_img
        if player_health >= 20:
            show healthbar_unit_2_left_img
        if player_health >= 30:
            show healthbar_unit_3_left_img
        if player_health >= 40:
            show healthbar_unit_4_left_img
        if player_health >= 50:
            show healthbar_unit_5_left_img
        if player_health >= 60:
            show healthbar_unit_6_left_img
        if player_health >= 70:
            show healthbar_unit_7_left_img
        if player_health >= 80:
            show healthbar_unit_8_left_img
        if player_health >= 90:
            show healthbar_unit_9_left_img
        if player_health >= 100:
            show healthbar_unit_10_left_img

        hide healthbar_unit_1_right_img
        hide healthbar_unit_2_right_img
        hide healthbar_unit_3_right_img
        hide healthbar_unit_4_right_img
        hide healthbar_unit_5_right_img
        hide healthbar_unit_6_right_img
        hide healthbar_unit_7_right_img
        hide healthbar_unit_8_right_img
        hide healthbar_unit_9_right_img
        hide healthbar_unit_10_right_img

        if opponent_health >= 10:
            show healthbar_unit_1_right_img
        if opponent_health >= 20:
            show healthbar_unit_2_right_img
        if opponent_health >= 30:
            show healthbar_unit_3_right_img
        if opponent_health >= 40:
            show healthbar_unit_4_right_img
        if opponent_health >= 50:
            show healthbar_unit_5_right_img
        if opponent_health >= 60:
            show healthbar_unit_6_right_img
        if opponent_health >= 70:
            show healthbar_unit_7_right_img
        if opponent_health >= 80:
            show healthbar_unit_8_right_img
        if opponent_health >= 90:
            show healthbar_unit_9_right_img
        if opponent_health >= 100:
            show healthbar_unit_10_right_img

    if combo > 0 and not match_end:
        show combo_text "Combo " + str(combo)
    else:
        hide combo_text

    show friendship_text str(friendship) at truecenter

    return

label round1_start:
    narrator "Coach is giving Max some advice before he steps into the ring." with fade

    coach "At the beginning of a match Inferno likes to stick to a pattern that's {b}three moves long{/b}. Pay attention and you should be able to figure it out."

    show goggles_img
    show inferno_img

    narrator "Max and Inferno step into the ring."

    announcer "...winner will be determined by the best of three rounds."

    announcer "Aaaand here are our fighters! Inferno versus... Goggles!"

    inferno "You look scared, Goggle Boy."

    max_character "..."

    inferno "Do not worry, boy. It will be over soon."

    hide goggles_img
    hide inferno_img
    show goggles_energy_img
    show inferno_fire_img

    show healthbar_left_img
    show healthbar_unit_1_left_img
    show healthbar_unit_2_left_img
    show healthbar_unit_3_left_img
    show healthbar_unit_4_left_img
    show healthbar_unit_5_left_img
    show healthbar_unit_6_left_img
    show healthbar_unit_7_left_img
    show healthbar_unit_8_left_img
    show healthbar_unit_9_left_img
    show healthbar_unit_10_left_img

    show healthbar_right_img
    show healthbar_unit_1_right_img
    show healthbar_unit_2_right_img
    show healthbar_unit_3_right_img
    show healthbar_unit_4_right_img
    show healthbar_unit_5_right_img
    show healthbar_unit_6_right_img
    show healthbar_unit_7_right_img
    show healthbar_unit_8_right_img
    show healthbar_unit_9_right_img
    show healthbar_unit_10_right_img

    call update_status

    show infinity_img

    announcer "Round 1, START!" with fade

    jump round1

label round1:
    call action("attack")

    if round_end:
        jump round2_start

    call action("attack")

    if round_end:
        jump round2_start

    call action("counter")

    if round_end:
        jump round2_start

    jump round1

label round2_start:
    call update_friendship
    python:
        round = 2
        round_end = False
        player_health = 100
        opponent_health = 100
        combo = 0
        max_combo = 0
    call update_status

    if won_round_1:
        coach "Great job, Max! But now that you figured out that pattern, Inferno will probably mix things up."
        coach "Later in the match he likes to use a longer, {b}six-move{/b} pattern. Don't slip up now!"
    else:
        coach "Don't worry too much about it, Max. You're just getting warmed up!"
        coach "Plus, I bet Inferno is going to stick with that {b}three-move{/b} pattern for the second round, so you have one more shot to figure it out."

    announcer "Round 2, START!" with fade

    if wins > 0:
        jump round2_changeup
    else:
        jump round2_same

label round2_same:
    call action("attack")

    if round_end:
        jump round3_start
    if match_end:
        jump after_round

    call action("attack")

    if round_end:
        jump round3_start
    if match_end:
        jump after_round

    call action("counter")

    if round_end:
        jump round3_start
    if match_end:
        jump after_round

    jump round2_same

label round2_changeup:
    call action("attack")

    if round_end:
        jump round3_start
    if match_end:
        jump after_round

    call action("attack")

    if round_end:
        jump round3_start
    if match_end:
        jump after_round

    call action("counter")

    if round_end:
        jump round3_start
    if match_end:
        jump after_round

    call action("attack")

    if round_end:
        jump round3_start
    if match_end:
        jump after_round

    call action("attack")

    if round_end:
        jump round3_start
    if match_end:
        jump after_round

    call action("throw")

    if round_end:
        jump round3_start
    if match_end:
        jump after_round

    jump round2_changeup

label round3_start:
    call update_friendship

    python:
        round = 3
        round_end = False
        player_health = 100
        opponent_health = 100
        combo = 0
        max_combo = 0

    call update_status

    if won_round_2:
        coach "See? I knew you could do it!"
        coach "But now that you figured out that pattern, Inferno will probably mix things up."
        coach "Later in the match he likes to use a longer, {b}six-move{/b} pattern. Don't slip up now!"
    else:
        coach "You can't win them all, right? But you'll make a comeback in the third round, I know it!"
        coach "Plus, I bet Inferno is going to stick with that {b}six-move{/b} pattern for the third round, so you have one more shot to figure it out."

    announcer "Round 3, START!" with fade

    jump round3

label round3:
    call action("attack")

    if round_end or match_end:
        jump after_round

    call action("attack")

    if round_end or match_end:
        jump after_round

    call action("counter")

    if round_end or match_end:
        jump after_round

    call action("attack")

    if round_end or match_end:
        jump after_round

    call action("attack")

    if round_end or match_end:
        jump after_round

    call action("throw")

    if round_end or match_end:
        jump after_round

    jump round3

label check_health:
    if opponent_health <= 0 or player_health <= 0:
        if opponent_health <= 0 and player_health <= 0:
            announcer "It's a draw!"
        elif player_health <= 0:
            $ losses += 1
            if losses >= 2:
                "That's two of three! The Inferno wins the match!"
                $ match_end = True
            else:
                "The Inferno wins this round!"
                $ round_end = True
        elif opponent_health <= 0:
            $ wins += 1
            if wins >= 2:
                "That's two of three! Goggles wins the match!"
                python:
                    match_end = True
                    won_match = True
            else:
                "Goggles wins this round!"
                python:
                    round_end = True
                    if round == 1:
                        won_round_1 = True
                    elif round == 2:
                        won_round_2 = True

    return

label action(opponent_action):
    call do_action(opponent_action)
    call check_health

    return

label do_action(opponent_action):

menu:
    "Strike":
        if opponent_action == "attack":
            python:
                player_health -= opponent_strike_dmg
                opponent_health -= player_strike_dmg
                combo = 0
                max_combo = max([max_combo, combo])
            call update_status
            narrator "Both fighters punch each other at the same time." with hpunch
        elif opponent_action == "counter":
            python:
                player_health -= opponent_block_dmg
                combo = 0
                max_combo = max([max_combo, combo])
            call update_status
            narrator "Goggles throws a punch but Inferno blocks it." with hpunch
        elif opponent_action == "throw":
            python:
                opponent_health -= player_strike_dmg
                combo += 1
                max_combo = max([max_combo, combo])
            call update_status
            "Inferno tries to grab Goggles but he gets punched instead" with hpunch
    "Block":
        if opponent_action == "attack":
            "Inferno throws a punch but Goggles blocks it." with hpunch
        elif opponent_action == "counter":
            "The fighters are both blocking and planning their next move."
        elif opponent_action == "throw":
            python:
                player_health -= opponent_throw_dmg
                combo = 0
                max_combo = max([max_combo, combo])
            call update_status
            "Goggles blocks, but Inferno manages to grab and throw him." with vpunch
    "Throw":
        if opponent_action == "attack":
            python:
                player_health -= opponent_strike_dmg
                combo = 0
                max_combo = max([max_combo, combo])
            call update_status
            "Goggles try to grab Inferno but gets punched when he's off-guard." with hpunch
        elif opponent_action == "counter":
            python:
                opponent_health -= player_throw_dmg
                combo += 1
                max_combo = max([max_combo, combo])
            call update_status
            "Inferno blocks, but Goggles manages to grab and throw him." with vpunch
        elif opponent_action == "throw":
            "Both fighters try to grab each other and tussle for a few seconds. Nobody gets hurt."

return

menu win_quote:
    "Compliment his fire hair":
        max_character "That was a great match! Super cool hair, by the way."
        $ friendship += 25
    "Insult his fire hair":
        max_character "I thought you were supposed to be tough. Turns out you're just an old guy trying to cover up his baldness with that stupid fire."
        $ friendship -= 25
    "Don't mention his fire hair":
        max_character "Phew, that was a tough one!"
        $ friendship += 10

return

label after_round:
    call update_friendship
    call update_status

    hide healthbar_left_img
    hide healthbar_unit_1_left_img
    hide healthbar_unit_2_left_img
    hide healthbar_unit_3_left_img
    hide healthbar_unit_4_left_img
    hide healthbar_unit_5_left_img
    hide healthbar_unit_6_left_img
    hide healthbar_unit_7_left_img
    hide healthbar_unit_8_left_img
    hide healthbar_unit_9_left_img
    hide healthbar_unit_10_left_img

    hide healthbar_right_img
    hide healthbar_unit_1_right_img
    hide healthbar_unit_2_right_img
    hide healthbar_unit_3_right_img
    hide healthbar_unit_4_right_img
    hide healthbar_unit_5_right_img
    hide healthbar_unit_6_right_img
    hide healthbar_unit_7_right_img
    hide healthbar_unit_8_right_img
    hide healthbar_unit_9_right_img
    hide healthbar_unit_10_right_img

    if won_match:
        hide inferno_fire_img
        hide goggles_energy_img
        show goggles_img

        narrator "Max catches his breath as Inferno struggles to stand back up." with fade
        call win_quote
        call update_status

        if friendship >= min_friendship:
            narrator "Max holds out his hand to help Inferno stand up."
            narrator "Inferno glares at him for a second before his expression softens."
            narrator "He grabs Max's hand and stands up."

            show inferno_img

            inferno "You are... strong. Stronger than I thought. It seems I have much to learn."
            inferno "Would you like to train with me sometime?"
        else:
            narrator "Inferno leaps back to his feet and storms off."

            show inferno_fire_img

            inferno "This is not over, Goggles Boy! The next time we fight, I will BURN you."
    else:
        hide goggles_energy_img
        hide inferno_fire_img
        show inferno_img

        narrator "Inferno catches his breath as Max struggles to stand back up."
        if friendship >= min_friendship:
            inferno "You did not win, but do not be sad, boy. You fought well."
            narrator "Inferno grabs onto Max's hand and pulls him up to a standing position."

            show goggles_img

            inferno "I like your style. Let's train together sometime."
        else:
            inferno "Pitiful. You are not worth my time, Goggles Boy."

    return
