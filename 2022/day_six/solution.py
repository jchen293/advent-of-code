def get_answer(data):
    data = data[0]
    exist = set()

    unique_length = 0
    i = 0
    while i < len(data):
        for index in range(i, len(data)):
            if data[index] in exist:
                unique_length = 0
                break
            exist.add(data[index])
            unique_length += 1
            if unique_length == 4:
                return index + 1
        exist.clear()
        i += 1


def get_answer2(data):
    data = data[0]
    exist = set()

    unique_length = 0
    i = 0
    while i < len(data):
        for index in range(i, len(data)):
            if data[index] in exist:
                unique_length = 0
                break
            exist.add(data[index])
            unique_length += 1
            if unique_length == 14:
                return index + 1
        exist.clear()
        i += 1
