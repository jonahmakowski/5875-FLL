from random import randint

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
    def __init__(self, suit, num, reason):
        self.suit = suit
        self.num = num
        self.reason = reason

    def __repr__(self):
        if self.num is not None:
            return '{}:{}:{}'.format(self.suit, self.num, self.reason)
        elif self.num is None:
            return '{}:{}'.format(self.suit, self.reason)


def rand_card_generator(): # for testing
    options = [{'suit': 'spades', 'number': '1'}, {'suit': 'spades', 'number': '2'}, {'suit': 'spades', 'number': '3'},
               {'suit': 'spades', 'number': '4'}, {'suit': 'spades', 'number': '5'}, {'suit': 'spades', 'number': '6'},
               {'suit': 'spades', 'number': '7'}, {'suit': 'spades', 'number': '8'}, {'suit': 'spades', 'number': '9'},
               {'suit': 'spades', 'number': '10'}, {'suit': 'spades', 'number': 'jack'}, {'suit': 'spades', 'number': 'queen'},
               {'suit': 'spades', 'number': 'king'}, {'suit': 'spades', 'number': 'ace'}, {'suit': 'hearts', 'number': '1'},
               {'suit': 'hearts', 'number': '2'}, {'suit': 'hearts', 'number': '3'}, {'suit': 'hearts', 'number': '4'},
               {'suit': 'hearts', 'number': '5'}, {'suit': 'hearts', 'number': '6'}, {'suit': 'hearts', 'number': '7'},
               {'suit': 'hearts', 'number': '8'}, {'suit': 'hearts', 'number': '9'}, {'suit': 'hearts', 'number': '10'},
               {'suit': 'hearts', 'number': 'jack'}, {'suit': 'hearts', 'number': 'queen'}, {'suit': 'hearts', 'number': 'king'},
               {'suit': 'hearts', 'number': 'ace'}, {'suit': 'diamonds', 'number': '1'}, {'suit': 'diamonds', 'number': '2'},
               {'suit': 'diamonds', 'number': '3'}, {'suit': 'diamonds', 'number': '4'}, {'suit': 'diamonds', 'number': '5'},
               {'suit': 'diamonds', 'number': '6'}, {'suit': 'diamonds', 'number': '7'}, {'suit': 'diamonds', 'number': '8'},
               {'suit': 'diamonds', 'number': '9'}, {'suit': 'diamonds', 'number': '10'}, {'suit': 'diamonds', 'number': 'jack'},
               {'suit': 'diamonds', 'number': 'queen'}, {'suit': 'diamonds', 'number': 'king'}, {'suit': 'diamonds', 'number': 'ace'},
               {'suit': 'clubs', 'number': '1'}, {'suit': 'clubs', 'number': '2'}, {'suit': 'clubs', 'number': '3'},
               {'suit': 'clubs', 'number': '4'}, {'suit': 'clubs', 'number': '5'}, {'suit': 'clubs', 'number': '6'},
               {'suit': 'clubs', 'number': '7'}, {'suit': 'clubs', 'number': '8'}, {'suit': 'clubs', 'number': '9'},
               {'suit': 'clubs', 'number': '10'}, {'suit': 'clubs', 'number': 'jack'}, {'suit': 'clubs', 'number': 'queen'},
               {'suit': 'clubs', 'number': 'king'}, {'suit': 'clubs', 'number': 'ace'}]
    result = []
    for _ in range(13):
        random_num = randint(0, len(options)-1)
        result.append(options[random_num])
        del options[random_num]
    print('Your random cards are:')
    print('---------------------------------------------')
    for card in result:
        print('{}:{}'.format(card['suit'], card['number']))
    print('---------------------------------------------')
    return result
