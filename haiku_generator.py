import random


syllabels_five = ["An old silent pond", "splash! Silence again", "Autumn moonlight", "into the chestnut",
"In the twilight rain", "A lovely sunset.", "Light of the moon", "Creep eastward.",
"Seems far away.", "A mountain village", "the sound of water.", "Night; and once again,",
"turns into rain.", "The summer river:", "goes through the water.", "A lightning flash:", "From across the lake,",
"Just friends:"]

syllabels_seven = ["A frog jumps into the pond", "a worm digs silently", "these brilliant-hued hibiscus -",
"A summer river being crossed", "with sandals in my hands!", "under the piled-up snow",
"the while I wait for you, cold wind", "between the forest trees", "Past the black winter trees,",
"on a terrace, eyes aglow."]



def generate_haiku():
    line1 = random.choice(syllabels_five)
    line3 = line1
    while line1 == line3:
        line3 = random.choice(syllabels_five)
    haiku = f"{line1} \n {random.choice(syllabels_seven)} \n {line3}"

    return haiku