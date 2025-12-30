def read_input(file_name):
    fresh_ingredient_ranges = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()

            if line == '':
                break

            parts = line.split('-')
            fresh_ingredient_ranges.append((int(parts[0].strip()), int(parts[1].strip())))

    return fresh_ingredient_ranges

def merge_ranges(fresh_ingredient_ranges):
    if not fresh_ingredient_ranges:
        return []

    # Sort ranges by start position
    fresh_ingredient_ranges.sort(key=lambda x: x[0])

    # Merge overlapping ranges
    merged_ranges = []

    for start, end in fresh_ingredient_ranges:
        if merged_ranges and start <= merged_ranges[-1][1] + 1:
            # Overlapping or adjacent, merge with the last range
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
        else:
            # Non-overlapping, add as new range
            merged_ranges.append((start, end))

    return merged_ranges

if __name__ == "__main__":
    fresh_ingredient_ranges = read_input('2025/day5/input.txt')

    # Sort ranges by start position
    fresh_ingredient_ranges.sort(key=lambda x: x[0])

    # Merge overlapping ranges
    merged_fresh_ingredient_ranges = merge_ranges(fresh_ingredient_ranges)

    fresh_ingredient_count = 0
    for (start, end) in merged_fresh_ingredient_ranges:
        fresh_ingredient_count += (end - start + 1)

    print("Quantity of fresh ingredient IDs:", fresh_ingredient_count)