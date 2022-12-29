def get_answer2(data):
    stacks = [
        ['L', 'N', 'W', 'T', 'D'],
        ['C', 'P', 'H'],
        ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J'],
        ['C', 'W', 'S', 'N', 'T', 'Q', 'L'],
        ['P', 'H', 'C', 'N'],
        ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B'],
        ['M', 'B', 'R', 'J', 'G', 'S', 'L'],
        ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T'],
        ['W', 'G', 'D', 'N', 'P', 'L']]

    result = ""
    for item in data:
        data_list = [int(x) for x in item.split() if x.isdigit()]
        quantity = data_list[0]
        from_index = data_list[1] - 1
        to_index = data_list[2] - 1
        length = len(stacks[from_index])
        sub_list = stacks[from_index][length-quantity:]
        del stacks[from_index][length-quantity:]
        stacks[to_index] = stacks[to_index] + sub_list

    for stack in stacks:
        result += stack[-1]
    print(result)


def get_answer(data):
    stacks = [
        ['L', 'N', 'W', 'T', 'D'],
        ['C', 'P', 'H'],
        ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J'],
        ['C', 'W', 'S', 'N', 'T', 'Q', 'L'],
        ['P', 'H', 'C', 'N'],
        ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B'],
        ['M', 'B', 'R', 'J', 'G', 'S', 'L'],
        ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T'],
        ['W', 'G', 'D', 'N', 'P', 'L']]

    result = ""
    for item in data:
        data_list = [int(x) for x in item.split() if x.isdigit()]
        quantity = data_list[0]
        from_index = data_list[1] - 1
        to_index = data_list[2] - 1
        for _ in range(quantity):
            value = stacks[from_index].pop()
            stacks[to_index].append(value)
    for stack in stacks:
        result += stack[-1]
    print(result)
