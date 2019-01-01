from collections import defaultdict
import re

def part1(fabric_input):
    """

    :return:
    """
    fabric = [[[] for _ in range(0, 10)] for _ in range(0, 10)]

    for id in fabric_input:
        raw_input = fabric_input[id]

        row_init = raw_input[0][0]
        row_n = row_init + raw_input[1][0]

        col_init = raw_input[0][1]
        col_n = col_init + raw_input[1][1]

        for row in range(row_init, row_n):
            for col in range(col_init, col_n):
                fabric[row][col].append(id)

    print_fabric(fabric)
    print(number_of_overclaimed_squares(fabric))

def number_of_overclaimed_squares(fabric):
    overclaimed_squares = 0

    for row in range(0, len(fabric)):
        for col in range(0, len(fabric[row])):
            if len(fabric[row][col]) >= 2:
                overclaimed_squares += 1


    return overclaimed_squares


def print_fabric(fabric):
    for row in fabric:
        print(row)

if __name__ == "__main__":
    file_path = "input.txt"
    file = open(file_path, "r")

    claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), file)

    m = defaultdict(list)
    overlaps = {}
    for (claim_number, start_x, start_y, width, height) in claims:
        overlaps[claim_number] = set()
        for i in range(start_x, start_x + width):
            for j in range(start_y, start_y + height):
                if m[(i, j)]:
                    for number in m[(i, j)]:
                        overlaps[number].add(claim_number)
                        overlaps[claim_number].add(number)
                m[(i, j)].append(claim_number)

    print("a", len([k for k in m if len(m[k]) > 1]))
    print("b", [k for k in overlaps if len(overlaps[k]) == 0][0])