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