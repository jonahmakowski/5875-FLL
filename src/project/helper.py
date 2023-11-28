"""
Card dictionary format:
[{'suit':'spades', 'number':'king'}, {'suit':'hearts', 'number':'10'}]

All cards are placed in a list in this format
"""


def point_calculator(cards):
    points_total = 0
    for item in cards:
        if item['number'] == 'jack':
            points_total += 1
        elif item['number'] == 'queen':
            points_total += 2
        elif item['number'] == 'king':
            points_total += 3
        elif item['number'] == 'ace':
            points_total += 4
    return points_total


"""
Suits are:
spades
diamonds
hearts
clubs
pass
NT
"""

class Bid:
    def __init__(self, suit, num=None):
        self.suit = suit
        self.num = num

    def __repr__(self):
        if self.num is not None:
            return '{}:{}'.format(self.suit, self.num)
        elif self.num is None:
            return self.suit
