import random

very_close_reactions = [
    "The creature jolts, visibly startled by how close you are!",
    "Its fur bristles — you're almost touching its thoughts!",
    "It stumbles back, eyes wide with surprise!"
]

close_reactions = [
    "The creature starts sweating nervously...",
    "It takes a cautious step backward, clearly uneasy.",
    "Its body tenses — you’re getting dangerously close."
]

medium_reactions = [
    "The creature shifts uncomfortably but doesn't seem alarmed.",
    "It watches you with cautious curiosity.",
    "Its tail twitches slightly, betraying mild concern."
]

distant_reactions = [
    "The creature observes you calmly, unthreatened.",
    "It tilts its head, amused by your attempt.",
    "It sits down, clearly in no rush to react."
]

far_reactions = [
    "The creature yawns. That guess didn’t even tickle its whiskers.",
    "It rolls its eyes in playful disappointment.",
    "It scratches itself lazily, unimpressed by your attempt."
]

warmer_reactions = [
    "Its ears perk up — you're getting warmer!",
    "It leans forward ever so slightly — progress!",
    "A spark flickers in its eyes. You’re close!"
]

colder_reactions = [
    "It looks away, unimpressed. That’s colder.",
    "The creature blinks slowly — not quite.",
    "It huffs and sits back down. You’ve lost ground."
]

neutral_reactions = [
    "It gives you a puzzled look — you’re no closer than before.",
    "Nothing changes. The creature just blinks.",
    "It stares at you, motionless. That didn’t change a thing."
]

def get_creature_reaction(current_diff, previous_diff):
    if current_diff == 0:
        return ""

    if current_diff == 1:
        reaction = random.choice(very_close_reactions)
    elif current_diff <= 3:
        reaction = random.choice(close_reactions)
    elif current_diff <= 7:
        reaction = random.choice(medium_reactions)
    elif current_diff <= 15:
        reaction = random.choice(distant_reactions)
    else:
        reaction = random.choice(far_reactions)

    if previous_diff is not None:
        if current_diff < previous_diff:
            reaction += " " + random.choice(warmer_reactions)
        elif current_diff > previous_diff:
            reaction += " " + random.choice(colder_reactions)
        else:
            reaction += " " + random.choice(neutral_reactions)

    return reaction
