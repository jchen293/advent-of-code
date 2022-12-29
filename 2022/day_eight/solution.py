def get_answer2(data):
    highest = 0
    for row in range(1, len(data) - 1):
        for column in range(1, len(data[row]) - 1):
            score = get_score(data, row, column)
            highest = max(highest, score)

    return highest


def get_score(grid, row, column):
    left, right, top, bottom = 0, 0, 0, 0

    # check the top
    for index in range(row - 1, -1, -1):
        top += 1
        if grid[index][column] >= grid[row][column]:
            break

    # check the bottom
    for index in range(row + 1, len(grid)):
        bottom += 1
        if grid[index][column] >= grid[row][column]:
            break

    # check the left
    for index in range(column - 1, -1, -1):
        left += 1
        if grid[row][index] >= grid[row][column]:
            break

    # check the right
    for index in range(column + 1, len(grid[0])):
        right += 1
        if grid[row][index] >= grid[row][column]:
            break

    return left * right * top * bottom


def get_answer(data):
    result = len(data) * 2 + (len(data[0]) * 2 - 4)
    for row in range(1, len(data) - 1):
        for column in range(1, len(data[row]) - 1):
            if is_visible(data, row, column):
                result += 1

    return result


def is_visible(grid, row, column):
    not_possible = 0
    # check the top
    for index in range(0, row):
        if grid[index][column] >= grid[row][column]:
            not_possible += 1
            break

    # check the bottom
    for index in range(row + 1, len(grid)):
        if grid[index][column] >= grid[row][column]:
            not_possible += 1
            break

    # check the left
    for index in range(0, column):
        if grid[row][index] >= grid[row][column]:
            not_possible += 1
            break

    # check the right
    for index in range(column + 1, len(grid[0])):
        if grid[row][index] >= grid[row][column]:
            not_possible += 1
            break

    return not_possible < 4
