"""
A function that advises a player on the best next move in a round of blackjack.
For now, just use 15 as a Hit/Stay Threshold.
>>> advise_player(10, 5)
15 Hit.

>>> advise_player('Q', 5)
15 Hit.

>>> advise_player('A', 'K')
21 Blackjack!

>>> advise_player('A', 'A')
12 Hit.

>>> advise_player('J', 'K')
20 Stay.

"""


def advise_player(card_1, card_2):
    face_cards = ['j', 'k', 'q']
    
    if str(card_1).lower() in face_cards:
        card_1 = 10
    elif str(card_1).lower() == 'a':
        card_1 = 11
    
    if str(card_2).lower() in face_cards:
        card_2 = 10
    elif str(card_2).lower() == 'a':
        if card_1 == 11:
            card_2 = 1
    
    total = card_1 + card_2

    if total < 16:
        return '{} Hit.'.format(total)
    elif total > 16 and total <= 20:
        return '{} Stay.'.format(total)
    elif total == 21:
        return '{} Blackjack!'.format(total)
    elif total > 21:
        return '{} Bust!'.format(total)





