# --- Part Two ---
# Now, the Elves just need help accessing as much of the paper as they can.
# Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?
#
# --- Problem Description ---
# Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:
# Initial state:
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# Remove 13 rolls of paper:
# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.
# Remove 12 rolls of paper:
# .......x..
# .@@.x.x.@x
# x@@@@...@@
# x.@@@@..x.
# .@.@@@@.x.
# .x@@@@@@.x
# .x.@.@.@@@
# ..@@@.@@@@
# .x@@@@@@@.
# ....@@@...
# Remove 7 rolls of paper:
# ..........
# .x@.....x.
# .@@@@...xx
# ..@@@@....
# .x.@@@@...
# ..@@@@@@..
# ...@.@.@@x
# ..@@@.@@@@
# ..x@@@@@@.
# ....@@@...
# Remove 5 rolls of paper:
# ..........
# ..x.......
# .x@@@.....
# ..@@@@....
# ...@@@@...
# ..x@@@@@..
# ...@.@.@@.
# ..x@@.@@@x
# ...@@@@@@.
# ....@@@...
# Remove 2 rolls of paper:
# ..........
# ..........
# ..x@@.....
# ..@@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@x.
# ....@@@...
# Remove 1 roll of paper:
# ..........
# ..........
# ...@@.....
# ..x@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...
# Remove 1 roll of paper:
# ..........
# ..........
# ...x@.....
# ...@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...
# Remove 1 roll of paper:
# ..........
# ..........
# ....x.....
# ...@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...
# Remove 1 roll of paper:
# ..........
# ..........
# ..........
# ...x@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...
# Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.
# Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?
#
# --- Correct Answer ---
# 8616
def read_input(file_name):
    paper_matrix = []
    with open(file_name, 'r') as file:
        paper_matrix = [line.strip() for line in file]
    return paper_matrix

def count_paper_around(paper_matrix, row, column):
    adjacent_papers = 0
    paper_matrix_rows = len(paper_matrix)
    paper_matrix_cols = len(paper_matrix[0]) if paper_matrix_rows > 0 else 0

    adjacent_offsets = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1),           (0, 1),
                        (1, -1),  (1, 0),  (1, 1)]

    for (i, j) in adjacent_offsets:
        adjacent_row, adjacent_col = row + i, column + j
        if 0 <= adjacent_row < paper_matrix_rows and 0 <= adjacent_col < paper_matrix_cols:
            if paper_matrix[adjacent_row][adjacent_col] == '@':
                adjacent_papers += 1

    return adjacent_papers

def retrieve_accessible_paper(paper_matrix):
    accessible_count = 0
    new_paper_matrix = []

    for row in range(len(paper_matrix)):
        new_paper_matrix.append(['x' for _ in range(len(paper_matrix[row]))])
        for col in range(len(paper_matrix[row])):
            new_paper_matrix[row][col] = paper_matrix[row][col]
            if paper_matrix[row][col] == '@':
                adjacent_papers = count_paper_around(paper_matrix, row, col)
                if adjacent_papers < 4:
                    accessible_count += 1
                    new_paper_matrix[row][col] = '.'

    return accessible_count, new_paper_matrix

if __name__ == "__main__":
    paper_matrix = read_input('2025/day4/input.txt')
    total_paper_rolls = 0
    while True:
        accessible_paper_count, paper_matrix = retrieve_accessible_paper(paper_matrix)
        total_paper_rolls += accessible_paper_count
        if accessible_paper_count == 0:
            break

    print(f"Number of accessible rolls of paper: {total_paper_rolls}")