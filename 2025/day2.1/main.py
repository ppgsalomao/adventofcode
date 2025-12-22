import math

def read_input(file_name='2025/day2.1/input.example.txt'):
    ranges = []
    with open(file_name, 'r') as f:
        line = f.readline().strip()
        pairs = line.split(',')
        
        for pair in pairs:
            ranges.append(pair.split('-'))

    return ranges

def find_invalid_ids(ranges):
    print("Ranges:", ranges)
    invalid_ids = []

    for (start, end) in ranges:
        invalid_ids.extend([num for num in range(int(start), int(end) + 1) if is_invalid_id(num)])
        
    return invalid_ids

def is_invalid_id(num):
    str_num = str(num)
    middle = len(str_num) // 2
    return len(str_num) % 2 == 0 and str_num[0:middle] == str_num[middle:middle*2]

if __name__ == "__main__":
    ranges = read_input('2025/day2.1/input.txt')
    invalid_ids = find_invalid_ids(ranges)
    print("Invalid IDs: ", invalid_ids)
    print("Sum of invalid IDs: ", sum(invalid_ids))