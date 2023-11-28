import helper


def first(cards):
    points = helper.point_calculator(cards)
    if points < 13:
        return helper.Bid('pass')
    spades = 0
    hearts = 0
    diamonds = 0
    clubs = 0
    for card in cards:
        if card['suit'] == 'spades':
            spades += 1
        elif card['suit'] == 'hearts':
            hearts += 1
        elif card['suit'] == 'diamonds':
            diamonds += 1
        elif card['suit'] == 'clubs':
            clubs += 1
        else:
            print('suit', card['suit'], 'does not exist')
            raise SyntaxError
    if (spades >= 3 and hearts >= 3) and (diamonds >= 3 and clubs >= 3) and points >= 15:
        return helper.Bid('NT', num='1')