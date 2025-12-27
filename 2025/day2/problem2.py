# --- Part Two ---
# --- History ---
# The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?
#
# --- Problem Description ---
# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
# From the same example as before:
# - 11-22 still has two invalid IDs, 11 and 22.
# - 95-115 now has two invalid IDs, 99 and 111.
# - 998-1012 now has two invalid IDs, 999 and 1010.
# - 1188511880-1188511890 still has one invalid ID, 1188511885.
# - 222220-222224 still has one invalid ID, 222222.
# - 1698522-1698528 still contains no invalid IDs.
# - 446443-446449 still has one invalid ID, 446446.
# - 38593856-38593862 still has one invalid ID, 38593859.
# - 565653-565659 now has one invalid ID, 565656.
# - 824824821-824824827 now has one invalid ID, 824824824.
# - 2121212118-2121212124 now has one invalid ID, 2121212121.
# Adding up all the invalid IDs in this example produces 4174379265.
# What do you get if you add up all of the invalid IDs using these new rules?
#
# --- Correct Answer ---
# Your puzzle answer was 31898925685.

def read_input(file_name):
    ranges = []
    with open(file_name, 'r') as f:
        line = f.readline().strip()
        pairs = line.split(',')
        
        for pair in pairs:
            ranges.append(pair.split('-'))

    return ranges

def find_invalid_ids(ranges):
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
    ranges = read_input('2025/day2/input.txt')
    invalid_ids = find_invalid_ids(ranges)
    print("Sum of invalid IDs: ", sum(invalid_ids))