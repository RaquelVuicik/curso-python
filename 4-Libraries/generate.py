import random

# moeda = random.choice(['cara', 'coroa'])
# print(moeda)

# number = random.randint(1, 10)
# print(number)

cards = ["Valete", "Dama", "Rei"]
random.shuffle(cards)
for card in cards:
    print(card)
