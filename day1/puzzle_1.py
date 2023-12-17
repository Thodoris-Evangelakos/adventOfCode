FILENAME = "input.txt"
TEST_FILENAME = "testinput1.txt"

def convertLineToValue(line: str) -> int:
    nums = []
    for character in line:
        if character.isdigit():
            nums.append(character)
    value = int(str(nums[0]) + str(nums[-1]))
    return value

def main():
    values = []
    with open(FILENAME, 'r+') as f:
        for line in f:
            values.append(convertLineToValue(line))
    value_sum = sum(values)
    print(value_sum)

if __name__ == "__main__":
    main()