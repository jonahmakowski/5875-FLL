import helper


def first(cards):
    points = helper.point_calculator(cards)
    # If you have less than 13 points pass
    if points < 13:
        return helper.Bid('pass', None, 'Less than 13 points')

    # Finding out how many of each suit you have
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

    # If you have an even hand, and 15 or more points, bid 1 NT
    if (spades >= 3 and hearts >= 3) and (diamonds >= 3 and clubs >= 3) and points >= 15:
        return helper.Bid('NT', '1', 'Balanced hand (at least three of each suit), and 15+ points')
    # If you have more spades than anything else, and have seven or more spades, bid 1 of spades
    elif spades >= 7 and (spades >= hearts and spades >= diamonds) and spades >= clubs:
        return helper.Bid('spades', '1', 'Most amount of spades and more than 7 spades')
    # If you have more hearts than anything else, and have seven or more hearts, bid 1 of hearts
    elif hearts >= 7 and (hearts >= spades and hearts >= diamonds) and hearts >= clubs:
        return helper.Bid('hearts', '1', 'Most amount of hearts and more than 7 hearts')
    # If you have more diamonds than anything else, and have five or more diamonds, bid 1 of diamonds
    elif diamonds >= 5 and (diamonds >= hearts and diamonds >= spades) and diamonds >= clubs:
        return helper.Bid('diamonds', '1', 'Most amount of diamonds and more than 5 diamonds')
    # If you have more clubs than anything else, and have five or more clubs, bid 1 of clubs
    elif clubs >= 5 and (clubs >= hearts and clubs >= spades) and clubs >= diamonds:
        return helper.Bid('clubs', '1', 'Most amount of clubs and more than 5 clubs')
    # Your cards don't fit in any of the other categories, so pass
    else:
        return helper.Bid('pass', None, 'TO BE FIXED!!! I dont know what to put here')