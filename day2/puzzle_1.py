"""Max values for each type of rock"""
RED = 12
GREEN = 13
BLUE = 14

TEST_INPUT = "test-input1.txt"
INPUT = "input.txt"

def fill_list_remainder_with_zeros(lst: list, length: int) -> list:
    """takes a list and returns a 'length' sized list, where the remainder of the list is 0s

    Args:
        lst (list): the list to be filled
        length (int): the length of the list to be returned

    Returns:
        list: the filled list
    """
    if length < len(lst):
        raise ValueError("\'length\' value smaller than list length")
    filled_list = [0 for i in range(length)]
    for n, item in enumerate(lst):
        filled_list[n] = item
    return filled_list

def check_if_game_is_legal(line: str) -> int:
    """_summary_

    Args:
        line (str): a line of the file

    Returns:
        int: The id of the game. If the game is illegal 0 is returned instead
    """
    _comp_ = line.split(":")
    game_id = int(_comp_[0].split(" ")[1])
    sets = _comp_[1].split(";")
    for single_set in sets:
        set_dict = {"red": 0, "green": 0, "blue": 0}
        value_color_pairs = single_set.split(",")
        for value_color_pair in value_color_pairs:
            _parts_ = value_color_pair.split(" ")
            value = int(_parts_[1])
            color = _parts_[2]

            match color:
                case 'red':
                    set_dict["red"] = value
                case 'green':
                    set_dict["green"] = value
                case 'blue':
                    set_dict["blue"] = value

        if set_dict['red'] > RED or set_dict['green'] > GREEN or set_dict['blue'] > BLUE:
            return 0
        #print(set_dict)
    #print(f"{'~'*10}LINE DONE{'~'*10}")
    return game_id

def main():
    """handles the program's main control flow
    """
    id_sum = 0
    with open(INPUT, 'r', encoding = "utf-8") as f:
        for line in f:
            id_sum += check_if_game_is_legal(line.rstrip())
    print(id_sum)


if __name__ == "__main__":
    main()
    