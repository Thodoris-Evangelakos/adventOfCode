FILENAME = "input1.txt"
TEST_FILENAME = "testinput2.txt"

NUMBERS_IN_LETTERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NUMS_DICT = {'1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine'}
REVERSE_NUMS_DICT = {NUMS_DICT[x]:x for x in NUMS_DICT}
DIGITS = [i for i in range(1,10)]

#den mporw na skeftw kapoia elegant lysh
#isws na ginetai eukola me regex
#twra thelei ligo bruteforcing kai high Os

def convertTextToNum(num_text: str) -> int:
    num = REVERSE_NUMS_DICT[num_text]
    return num

def convertLineToValue(line: str) -> int:
    list_of_chars = []
    for char in line:
        list_of_chars.append(char)
    
    nums = []        
    starting_index = 0
    _end_flag_ = False
    _chars_ = []
    #possible error, isws na thelei len(foo)+-1?
    while starting_index < len(list_of_chars) and (not _end_flag_):
        for i in range(starting_index, len(list_of_chars)):
            
            if list_of_chars[i].isdigit():
                #print("found digit")
                starting_index = i+1
                _chars_ = []
                nums.append(list_of_chars[i])
                break
            
            _chars_.append(list_of_chars[i])
            
            for item in NUMBERS_IN_LETTERS:
                _idx_ = ''.join(_chars_).find(item)
                if _idx_ != -1:
                    #print("found number as letters")
                    starting_index = (_idx_ + starting_index)+1
                    #starting_index = _idx_+1
                    _chars_ = []
                    nums.append(convertTextToNum(item))
                    break
            #switching this to >= from == fixed the 29th (and final) iteration of the infinite loop
            if i >= len(list_of_chars)-2:
                _end_flag_ = True
                break
            if len(_chars_) == 0:
                break
            
        #break

        
            
    value = int(str(nums[0]) + str(nums[-1]))
    return value

def main():
    values = []
    with open(FILENAME, 'r+') as f:
        for line in f:
            values.append(convertLineToValue(line))
    value_sum = sum(values)
    #print(values)
    print(value_sum)

if __name__ == "__main__":
    main()