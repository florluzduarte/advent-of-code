import re


def main():
    grid = get_grid("grid_data.txt")
    columns = get_columns_data(grid)
    forward_diag, backward_diag = get_diag_data(grid)
    count = get_total_xmas(grid, columns, forward_diag, backward_diag)
    print(count)


def get_grid(file):
    grid_rows = []
    with open(file) as grid:
        for row in grid:
            grid_rows.append(row.strip())
    return grid_rows


def get_grid_dimensions(grid):
    height = len(grid)
    width = len(grid[0])
    return height, width


def get_horizontal_xmas(grid):
    forwards = 0
    backwards = 0
    for row in grid:
        match_forward = re.findall(r"(XMAS)", row)
        forwards += len(match_forward)
        match_backwards = re.findall(r"(SAMX)", row)
        backwards += len(match_backwards)
    return forwards + backwards


def get_columns_data(grid):
    columns = []
    for i in range(0, len(grid)):
        column = []
        for row in grid:
            letter = row[i]
            column.append(letter)
        columns.append("".join(column))
    return columns


def get_vertical_xmas(grid_columns):
    return get_horizontal_xmas(grid_columns)


def get_diag_data(grid):
    max_col = len(grid[0])
    max_row = len(grid)
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1
    for x in range(max_col):
        for y in range(max_row):
            fdiag[x+y].append(grid[y][x])
            bdiag[x-y-min_bdiag].append(grid[y][x])
    fdiag_str = []
    for row in fdiag:
        fstr = ""
        for letter in row:
            fstr = fstr + letter
        fdiag_str.append(fstr)
    bdiag_str = []
    for row in bdiag:
        bstr = ""
        for letter in row:
            bstr = bstr + letter
        bdiag_str.append(bstr)
    return fdiag_str, bdiag_str


def get_diag_xmas(fdiag, bdiag):
    return get_horizontal_xmas(fdiag) + get_horizontal_xmas(bdiag)


def get_total_xmas(grid, cols, fdiag, bdiag):
    horizontal_count = get_horizontal_xmas(grid)
    vertical_count = get_vertical_xmas(cols)
    diag_count = get_diag_xmas(fdiag, bdiag)
    return horizontal_count + vertical_count + diag_count


if __name__ == "__main__":
    main()
