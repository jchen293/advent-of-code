def get_answer(data):
    temp_list = []
    for i in data:
        if i == "":
            temp_list.append(temp_value)
            temp_value = 0
        else:
            temp_value += int(i)

    temp_list.sort()

    print(max(temp_list), sum(temp_list[-3:]))
