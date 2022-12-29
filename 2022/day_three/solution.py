import string


def get_answer2(data):
    point = 0
    mapper = dict((key, 1)
                  for key in string.ascii_lowercase + string.ascii_uppercase)
    exist = set()
    for index, item in enumerate(data):
        for char in item:
            if char in exist:
                continue
            else:
                mapper[char] += 1
                exist.add(char)
        exist.clear()
        if (index + 1) % 3 == 0:
            point += get_common(mapper)
            mapper = dict((key, 1)
                          for key in string.ascii_lowercase + string.ascii_uppercase)
    print(point)


def get_common(data):
    result = None
    occurence = 0
    for k, v in data.items():
        if v > occurence:
            occurence = v
            result = k
    return get_point(result)


def get_answer(data):
    point = 0
    for string in data:
        half_point = len(string) // 2
        first_half = string[0: half_point]
        second_half = string[half_point:]

        exist = set()

        for char in first_half:
            exist.add(char)

        for char in second_half:
            if char in exist:
                point += get_point(char)
                break
    print(point)


def get_point(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38
