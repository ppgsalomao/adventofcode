import math

def read_input(file_name='2025/day2.2/input.example.txt'):
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

    for chunk_amount in range(2, len(str_num)+1):
        if len(str_num) % chunk_amount != 0:
            continue

        chunk_size = len(str_num) // chunk_amount
        chunks = [str_num[j:j+chunk_size] for j in range(0, len(str_num), chunk_size)]

        if len(set(chunks)) == 1:
            return True

    return False

if __name__ == "__main__":
    ranges = read_input('2025/day2.2/input.txt')
    invalid_ids = find_invalid_ids(ranges)
    print("Invalid IDs: ", invalid_ids)
    print("Sum of invalid IDs: ", sum(invalid_ids))