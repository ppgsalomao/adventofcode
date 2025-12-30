def read_input(file_name):
    fresh_ingredient_ranges = []
    ingredient_ids = []

    reading_fresh_ingredient_ranges = True

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()

            if line == '':
                reading_fresh_ingredient_ranges = False
                continue

            if reading_fresh_ingredient_ranges:
                parts = line.split('-')
                fresh_ingredient_ranges.append((int(parts[0].strip()), int(parts[1].strip())))

            else:
                ingredient_ids.append(int(line))

    return fresh_ingredient_ranges, ingredient_ids

def is_fresh_ingredient(ingredient_id, fresh_ingredient_ranges):
    for (start, end) in fresh_ingredient_ranges:
        if start <= ingredient_id <= end:
            return True
    return False

if __name__ == "__main__":
    fresh_ingredient_ranges, ingredient_ids = read_input('2025/day5/input.txt')

    fresh_ingredient_ids = set()
    for ingredient_id in ingredient_ids:
        if is_fresh_ingredient(ingredient_id, fresh_ingredient_ranges):
            fresh_ingredient_ids.add(ingredient_id)

    print("Quantity of fresh ingredient IDs:", len(fresh_ingredient_ids))