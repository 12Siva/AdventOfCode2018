def do_react(a, b):
    """
    Determine if a and b react
    :param a: char
    :param b: char
    :return: true if they react, false otherwise
    """
    return (a.lower() == b.lower() and
            ((a.isupper() and b.islower()) or
             (a.islower() and b.isupper())))


def part1(input_str: str):
    """
    Part 1
    :param input_str: polymer
    :return: length of completely reacted polymer
    """
    buffer = []
    for char in input_str:
        if buffer and do_react(char, buffer[-1]):
            buffer.pop()
        else:
            buffer.append(char)

    return len(buffer)


def part2(polymer: str):
    """
    Part 2
    :param polymer: input polymer string
    :return: the smallest length polymer string removing one agent and fully reacting the polymer
    """
    agents = set([char.lower() for char in polymer])
    min_length = 100000000000
    for agent in agents:
        tmp_polymer = polymer.replace(agent, "").replace(agent.upper(), "")
        reacted_len = part1(tmp_polymer)
        #print("{}:{}".format(agent, reacted_len))
        if min_length > reacted_len:
            min_length = reacted_len

    return min_length


def part2_one_liner(polymer: str):
    """
    Part 2 written in one line
    :param polymer: input polymer string
    :return: the smallest length polymer string removing one agent and fully reacting the polymer
    """
    agents = set([char.lower() for char in polymer])
    return min([part1(polymer.replace(agent, "").replace(agent.upper(), "")) for agent in agents])


if __name__ == "__main__":
    file = open('input.txt', 'r')
    raw_input = file.read().strip()

    # answer1 = part1(raw_input)
    # print("Answer to part 1: {}".format(answer1))

    answer2 = part2(raw_input)
    print("Answer to part 2: {}".format(answer2))