# --- Day 4: Printing Department ---
# --- History ---
# You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).
# Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.
# "Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."
# If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.
# 
# --- Problem Description ---
# The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.
# For example:
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
# The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
# In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):
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
# Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
#
# --- Correct Answer ---
# 1433

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

def count_accessible_paper(paper_matrix):
    accessible_count = 0

    for row in range(len(paper_matrix)):
        for col in range(len(paper_matrix[row])):
            if paper_matrix[row][col] == '@':
                adjacent_papers = count_paper_around(paper_matrix, row, col)
                if adjacent_papers < 4:
                    accessible_count += 1

    return accessible_count


if __name__ == "__main__":
    paper_matrix = read_input('2025/day4/input.txt')
    accessible_paper_count = count_accessible_paper(paper_matrix)
    print(f"Number of accessible rolls of paper: {accessible_paper_count}")