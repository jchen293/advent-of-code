def get_answer2(data):
    result = 0
    for item in data:
        pairs = item.split(",")
        if overlap(pairs[0], pairs[1]) or overlap(pairs[1], pairs[0]):
            result += 1
    print(result)


def get_answer(data):
    result = 0
    for item in data:
        pairs = item.split(",")
        if is_subset(pairs[0], pairs[1]) or is_subset(pairs[1], pairs[0]):
            result += 1
    print(result)


def overlap(set_one, set_two):
    set_one_pair = set_one.split('-')
    set_two_pair = set_two.split('-')

    result = int(set_one_pair[1]) >= int(set_two_pair[0]) and int(
        set_one_pair[1]) <= int(set_two_pair[1])

    return result


def is_subset(set_one, set_two):
    set_one_pair = set_one.split('-')
    set_two_pair = set_two.split('-')

    result = int(set_one_pair[0]) <= int(set_two_pair[1]) and int(set_one_pair[0]) >= int(
        set_two_pair[0]) and int(set_one_pair[1]) <= int(set_two_pair[1])
    return result
