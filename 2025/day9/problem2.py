from collections import deque

def read_input(file_name):
    red_tiles = []
    with open(file_name, 'r') as file:
        for line in file:
            line_coordinates = line.strip().split(',')
            red_tiles.append((int(line_coordinates[0]), int(line_coordinates[1])))

    return red_tiles

def generate_compressed_grid(red_tiles, compressed_xs=None, compressed_ys=None):
    grid = [[0] * len(compressed_ys) for _ in range(len(compressed_xs))]
    for (x1, y1), (x2, y2) in zip(red_tiles, red_tiles[1:] + red_tiles[:1]):
        cx1, cx2 = sorted([compressed_xs.index(x1), compressed_xs.index(x2)])
        cy1, cy2 = sorted([compressed_ys.index(y1), compressed_ys.index(y2)])
        for cx in range(cx1, cx2 + 1):
            for cy in range(cy1, cy2 + 1):
                grid[cx][cy] = 1

    # Flood fill from outside to find all non-red or green tiles
    outside = {(-1, -1)}
    queue = deque(outside)

    while len(queue) > 0:
        tx, ty = queue.popleft()
        for nx, ny in [(tx - 1, ty), (tx + 1, ty), (tx, ty - 1), (tx, ty + 1)]:
            if nx < -1 or ny < -1 or nx > len(grid) or ny > len(grid[0]): continue
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1: continue
            if (nx, ny) in outside: continue
            outside.add((nx, ny))
            queue.append((nx, ny))

    # Mark all non-outside tiles as red/green (1)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in outside:
                grid[x][y] = 1

    return grid

def generate_prefix_sum_grid(grid):
    psa = [[0] * len(row) for row in grid]
    for x in range(len(psa)):
        for y in range(len(psa[0])):
            left = psa[x - 1][y] if x > 0 else 0
            top = psa[x][y - 1] if y > 0 else 0
            topleft = psa[x - 1][y - 1] if x > 0 < y else 0
            psa[x][y] = left + top - topleft + grid[x][y]

    return psa

def is_valid_rectangle(compressed_xs, compressed_ys, prefix_sum_grid, vertex1, vertex2):
    compressed_x1, compressed_x2 = sorted([compressed_xs.index(vertex1[0]), compressed_xs.index(vertex2[0])])
    compressed_y1, compressed_y2 = sorted([compressed_ys.index(vertex1[1]), compressed_ys.index(vertex2[1])])

    left = prefix_sum_grid[compressed_x1 - 1][compressed_y2] if compressed_x1 > 0 else 0
    top = prefix_sum_grid[compressed_x2][compressed_y1 - 1] if compressed_y1 > 0 else 0
    topleft = prefix_sum_grid[compressed_x1 - 1][compressed_y1 - 1] if compressed_x1 > 0 < compressed_y1 else 0
    count = prefix_sum_grid[compressed_x2][compressed_y2] - left - top + topleft

    return count == (compressed_x2 - compressed_x1 + 1) * (compressed_y2 - compressed_y1 + 1)

def calculate_rectangle_area(vertex1, vertex2):
    return (abs(vertex1[0] - vertex2[0]) + 1) * (abs(vertex1[1] - vertex2[1]) + 1)

def find_largest_red_tile_area(red_tiles):
    max_area = -1
    max_rectangle = None

    compressed_xs = sorted({ x for x, _ in red_tiles })
    compressed_ys = sorted({ y for _, y in red_tiles })

    grid = generate_compressed_grid(red_tiles, compressed_xs, compressed_ys)
    prefix_sum_grid = generate_prefix_sum_grid(grid)

    for i, (x1, y1) in enumerate(red_tiles):
        for x2, y2 in red_tiles[:i]:
            if is_valid_rectangle(compressed_xs, compressed_ys, prefix_sum_grid, (x1, y1), (x2, y2)):
                area = calculate_rectangle_area((x1, y1), (x2, y2))
                if area > max_area:
                    max_area = area
                    max_rectangle = ((x1, y1), (x2, y2))
                    print(f"Max rectangle found: {max_rectangle} with area {max_area}")

    return max_area, max_rectangle

if __name__ == "__main__":
    red_tiles = read_input('2025/day9/input.txt')
    print("Finding largest red tile area...")
    largest_area, largest_rectangle = find_largest_red_tile_area(red_tiles)
    print(f"Largest red tile area: {largest_area}")
    print(f"Largest rectangle corners: {largest_rectangle}")
