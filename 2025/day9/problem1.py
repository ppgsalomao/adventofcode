def read_input(file_name):
    red_tile_positions = []

    with open(file_name, 'r') as file:
        for line in file:
            line_coordinates = line.strip().split(',')
            red_tile_positions.append((int(line_coordinates[0]), int(line_coordinates[1])))

    return red_tile_positions

def find_largest_red_tile_area(red_tile_positions):
    max_area = -1
    for i in range(len(red_tile_positions)):
        for j in range(len(red_tile_positions)):
            if i < j:
                max_area = max(max_area, (abs(red_tile_positions[i][0] - red_tile_positions[j][0]) + 1) * (abs(red_tile_positions[i][1] - red_tile_positions[j][1]) + 1))
    return max_area    


if __name__ == "__main__":
    red_tile_positions = read_input('2025/day9/input.txt')
    largest_area = find_largest_red_tile_area(red_tile_positions)
    print(f"Largest red tile area: {largest_area}")