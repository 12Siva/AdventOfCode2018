from collections import Counter, defaultdict
import difflib


# Part 1
def part1():
    """

    :return:
    """
    file_path = "input.txt"

    file = open(file_path, "r")

    ids = [line.strip("\n") for line in file]

    two_char_count = 0
    three_char_count = 0

    for id in ids:
        char_count = Counter(id)
        two_char_found = False
        three_char_found = False

        for char in char_count:
            if (char_count[char] == 2) and (not two_char_found):
                two_char_count += 1
                two_char_found = True
            if (char_count[char] == 3) and (not three_char_found):
                three_char_count += 1
                three_char_found = True

    print(two_char_count * three_char_count)

# Part 2
def part2():
    """

    :return:
    """
    file_path = "input.txt"

    file = open(file_path, "r")

    ids = [line.strip("\n") for line in file]
    result = ""

    for x in range(0, len(ids)):
        for y in range(x, len(ids)):
            left = ids[x]
            right = ids[y]

            diff = difflib.ndiff(left, right)
            diff_count = 0

            for _, s in enumerate(diff):
                if (s[0] != " "):
                    diff_count += 1

            if diff_count == 2:
                diff = difflib.ndiff(left, right)
                for s in diff:
                    if (s[0] == " "):
                        result += s[-1]

    print(result)

part2()