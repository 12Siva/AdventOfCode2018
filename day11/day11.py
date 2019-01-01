import numpy as np


def get_hundreds_place(raw_input):
    """

    :param raw_input:
    :return:
    """
    result = (raw_input // 100) % 10
    return result


def compute_power_level(x_coordinate, y_coordinate):
    """

    :param x_coordinate:
    :param y_coordinate:
    :return:
    """
    serial_number = 1309

    # 1. rack id = x coordinate plus 10
    rack_id = x_coordinate + 1 + 10

    # 2. power level = rack id * y coordinate
    power_level = rack_id * (y_coordinate + 1)

    # 3. power level = power level + serial number
    power_level += serial_number

    # 4. power level = power level * rack id
    power_level *= rack_id

    # 5. power level = only the hundreds place of the power level
    power_level = get_hundreds_place(power_level)

    # 6. power level = power level - 5
    power_level -= 5

    return power_level

def part1():
    """
    :return:
    """
    grid = np.fromfunction(compute_power_level, (300, 300))

    print(grid)

    for width in range(3, 300):
        windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
        maximum = int(windows.max())
        location = np.where(windows == maximum)

        print(width, maximum, location[0][0] + 1, location[1][0] + 1)

    return None


if __name__ == "__main__":
    fuel_cell = (2, 2)

    grid = np.fromfunction(compute_power_level, (300, 300))
    print(grid)
