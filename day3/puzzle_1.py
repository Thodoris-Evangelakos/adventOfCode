'''Imports and Globals'''
import re

TEST_INPUT = "test_input.txt"
INPUT = "input.txt"
TEST_LINE_LENGTH = 10
LINE_LENGTH = 140
EMPTY_TEST_LINE = "."*10
EMPTY_LINE = "."*140

def is_symbol(char: str) -> bool:
    """Checks if a character is considered a symbol

    Args:
        char (str): The character in question

    Returns:
        bool: Whether the character is a symbol or not idfk what to write here
    """
    symbol_list = ['+','*','#','$']
    return (not char.isdigit() and char != '.') or (char in symbol_list)

def find_integer_indices(line: str) -> tuple:
    indices = [(m.start(0), m.end(0)-1, int(line[m.start(0):m.end(0)])) for m in re.finditer(r"\d+", line)]
    return indices


def is_adj_to_symbol(lines: list, indices: list) -> int:
    line_sum = 0
    for pair in indices:
        for i in range(pair[0], pair[1]+1): #care
            if is_symbol(lines[0][i]) or is_symbol(lines[2][i]):
                line_sum += pair[2]
                print(pair[2])
                break
        if pair[0] > 0:
            if is_symbol(lines[0][pair[0]-1]) or is_symbol(lines[1][pair[0]-1]) or is_symbol(lines[2][pair[0]-1]):
                line_sum += pair[2]
                print(pair[2])
                continue
        if pair[1] < LINE_LENGTH-1:
            if is_symbol(lines[0][pair[1]+1]) or is_symbol(lines[1][pair[1]+1]) or is_symbol(lines[2][pair[1]+1]):
                line_sum += pair[2]
                print(pair[2])
                continue
    return line_sum

def main():
    """controls main program control flow
    """
    part_sum = 0
    with open(INPUT, 'r', encoding = 'utf-8') as f:
        #lines = [line for line in f] -> Unnecessary use of a comprehension, use list(f) instead.
        lines = list(f)
        for i in range(len(lines)):
            line_set = [lines[n].strip("\n") for n in range(i-1,i+2) if n > -1 and n < len(lines)]
            if i == 0:
                line_set.insert(0, EMPTY_LINE)
            elif i == len(lines)-1:
                line_set.append(EMPTY_LINE)
            else:
                pass
            part_sum += is_adj_to_symbol(line_set, find_integer_indices(line_set[1]))
        print(part_sum)

if __name__ == "__main__":
    main()
