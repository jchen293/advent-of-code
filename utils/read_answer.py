from typing import List


def open_input(input_path: str) -> List[str]:
    with open(input_path, 'r') as f:
        lines = f.readlines()

    line_data = lines[:-1] if lines[-1] == '' else lines
    data = [line_item.replace('\n', '').strip() for line_item in line_data]

    return data


def open_input_literal(input_path: str) -> str:
    with open(input_path, 'r') as f:
        lines = f.read()

    return lines
