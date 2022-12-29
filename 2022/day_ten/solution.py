from utils.read_answer import open_input


def main():
    # TODO: Change this string
    data = open_input('sample.txt')
    answer_1 = print(get_answer(data))
    #answer_2 = print(get_answer2(data))

    return None


def get_answer(data):
    cycles = 0
    x = 1
    result = 0
    check = [20, 60, 100, 140, 180, 220]

    for index, program in enumerate(data):
        if program == "noop":
            cycles += 1
            if cycles in check:
                result += cycles * x
        else:
            for i in range(2):
                cycles += 1
                if cycles in check:
                    result += x * cycles
            x += int(program.split()[1])

    return result


if __name__ == '__main__':
    main()
