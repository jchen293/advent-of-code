from typing import List


def open_input(input_path: str) -> List[str]:
    """Opens and sanitizes the `input.txt` file for the day reading in each line as an element of a list.
    - Remove any extra lines at the end of the input files (if present, due to auto-formatting)
    - Remove newline characters for individual element strings
    - Strip any whitespace
    """
    with open(input_path, 'r') as f:
        lines = f.readlines()

    line_data = lines[:-1] if lines[-1] == '' else lines
    data = [line_item.replace('\n', '').strip() for line_item in line_data]

    return data


def open_input_literal(input_path: str) -> str:
    """Opens the `input.txt` file literally without sanitizing the data or converting it to a list.
    This should be considered the "legacy" approach or only used when the input data has a structure
    that requires custom parsing.
    """
    with open(input_path, 'r') as f:
        lines = f.read()

    return lines


# def main():
#     # TODO: Change this string
#     data = open_input('2022/day_nine/sample.txt')
#     answer_1 = print(get_answer(data))
#     #answer_2 = print(get_answer2(data))

#     return None