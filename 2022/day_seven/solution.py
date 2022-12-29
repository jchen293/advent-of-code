def get_answer(data):
    pass


def parse_helper(data):
    if "dir" in data:
        return data.split(" ")[1]
    else:
        return int(data.split(" ")[0])
