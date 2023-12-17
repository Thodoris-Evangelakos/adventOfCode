"""Imports"""
import sys
import re

"""Globals"""
MAX_INT = sys.maxsize
TEST_INPUT = "test-input1.txt"
INPUT = "input.txt"

def find_smallest_num(line: str) -> int:
    _data_ = line.split(":")[1].strip()
    pairs = re.split('; |, ', _data_)
    minimum_game_values = {"red": 0, "green": 0, "blue": 0}
    #print(pairs)
    for pair in pairs:
        _tmp_ = pair.split(" ")
        value = int(_tmp_[0])
        color = _tmp_[1]

        match color:
            case 'red':
                if value > minimum_game_values["red"]:
                    minimum_game_values["red"] = value
            case 'green':
                if value > minimum_game_values["green"]:
                    minimum_game_values["green"] = value
            case 'blue':
                if value > minimum_game_values["blue"]:
                    minimum_game_values["blue"] = value
        #print(f"\n\npair:{pair}\nvalue: {value}, color: {color}")
    total = 1
    for key, value in minimum_game_values.items():
        total *= value
    #print(total)
    return total

def main():
    """handles the program's main control flow
    """
    num_sum = 0
    with open(INPUT, 'r', encoding = 'utf-8') as f:
        for line in f:
            print(line)
            num_sum += find_smallest_num(line.rstrip())
    print(num_sum)


if __name__ == "__main__":
    main()
