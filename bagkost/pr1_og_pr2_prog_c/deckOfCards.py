import random as rand
from emoji import emojize

ranks = [str(i) for i in range(2,11)] + ["guard","princess","prince","A"]
ranks[-4:-1] = [emojize(f":{rank}:") for rank in ranks[-4:-1]]



suits = ["heart_suit", "club_suit", "diamond_suit", "spade_suit"]
suits = [emojize(f":{suit}:") for suit in suits]

deck_of_cards = ["{0} of {1}".format(rank, suit) for suit in suits for rank in ranks]
rand.shuffle(deck_of_cards)

print(deck_of_cards)

