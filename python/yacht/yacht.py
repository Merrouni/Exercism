# Score categories
# Change the values as you see fit
YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

dict = {ONES: 1, TWOS: 2, THREES: 3, FOURS: 4, FIVES: 5, SIXES: 6}

def score(dice, category):
    if category == YACHT:
        if isYacht(dice):
            return 50
        
    if dict.get(category) != None:    
        return dice.count(dict[category])*dict[category]
    
    if category == FULL_HOUSE:
        if not isFourOfAKind(dice) and len(set(dice)) == 2:
            return sum(dice)
        
    if category == FOUR_OF_A_KIND:
        if dice.count(dice[0]) >= 4:
            return 4*dice[0]
        elif dice.count(dice[1]) >= 4:
            return 4*dice[1]
        
    if category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        
    if category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        
    if category == CHOICE:
        return sum(dice)

    return 0

def isYacht(dice):
    return dice.count(dice[0]) == 5

def isFourOfAKind(dice):
    return dice.count(dice[0]) >= 4 or dice.count(dice[1]) == 4
