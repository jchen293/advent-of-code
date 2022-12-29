def get_answer2(data):
    point = 0

    for game in data:
        if game[2] == 'X':  # lost
            point += helper2(False, game[0]) + 0
        elif game[2] == 'Y':  # tie
            point += helper2(None, game[0]) + 3
        elif game[2] == 'Z':  # win
            point += helper2(True, game[0]) + 6
    print(point)


def helper2(win, char):
    if win == True:
        if char == 'A':
            return 2
        elif char == 'B':
            return 3
        else:
            return 1
    elif win == None:
        return helper(char)
    else:
        if char == 'A':
            return 3
        elif char == 'B':
            return 1
        else:
            return 2


def get_answer(data):
    point = 0

    for game in data:
        index_one = helper(game[0])
        index_two = helper(game[2])

        # 1 - rock
        # 2 - paper
        # 3 - Scissors
        if index_one == index_two:
            point += index_two + 3
        elif index_one == 1 and index_two == 2:
            point += index_two + 6
        elif index_one == 1 and index_two == 3:
            point += index_two + 0
        elif index_one == 2 and index_two == 3:
            point += index_two + 6
        elif index_one == 3 and index_two == 1:
            point += index_two + 6
        elif index_one == 2 and index_two == 1:
            point += index_two + 0
        elif index_one == 3 and index_two == 2:
            point += index_two + 0

    print(point)


def helper(character):
    res = 0
    if character == 'A' or character == 'X':
        res = 1
    elif character == 'B' or character == 'Y':
        res = 2
    elif character == 'C' or character == 'Z':
        res = 3

    return res
