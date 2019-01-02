from utils.decorators import time_it


def get_next_recipe_values(recipes, first_elf, second_elf):
    """
    :param recipes:
    :param first_elf:
    :param second_elf:
    :return:
    """
    next_recipes = []
    raw_recipe_value = recipes[first_elf] + recipes[second_elf]

    if raw_recipe_value >= 10:
        next_recipes.append(1)
        next_recipes.append(raw_recipe_value - 10)
    else:
        next_recipes.append(raw_recipe_value)

    return next_recipes


def get_next_recipe(recipes, elf):
    """

    :param recipes:
    :param elf:
    :return:
    """

    current_recipe = recipes[elf]
    raw_next_recipe = elf + current_recipe + 1

    next_recipe = raw_next_recipe % len(recipes)

    # print("{} : {} : {}".format(recipes, raw_next_recipe, next_recipe))
    return next_recipe

@time_it
def part1(num_of_recipes):
    """

    :param num_of_recipes:
    :return:
    """
    recipes = [3, 7]
    first_elf = 0
    second_elf = 1

    while len(recipes) < input + 2000:
        next_recipes = get_next_recipe_values(recipes, first_elf, second_elf)

        [recipes.append(ele) for ele in next_recipes]

        # print_recipes(recipes, first_elf, second_elf)
        first_elf = get_next_recipe(recipes, first_elf)
        second_elf = get_next_recipe(recipes, second_elf)

        # print_recipes(recipes, first_elf, second_elf)
        # print("*" * 250)

    ten_recipes = recipes[num_of_recipes:num_of_recipes + 10]
    return ten_recipes

@time_it
def part2(num_of_recipes):
    """

    :param num_of_recipes:
    :return:
    """
    recipe_list = [int(recipe) for recipe in str(num_of_recipes)]

    recipes = [3, 7]
    first_elf = 0
    second_elf = 1

    while True:
        next_recipes = get_next_recipe_values(recipes, first_elf, second_elf)

        [recipes.append(ele) for ele in next_recipes]

        first_elf = get_next_recipe(recipes, first_elf)
        second_elf = get_next_recipe(recipes, second_elf)

        if recipes[-len(recipe_list):] == recipe_list or recipes[-len(recipe_list) - 1:-1] == recipe_list:
            break

    return ''.join(map(str, recipes)).index(''.join(map(str, recipe_list)))


def print_recipes(recipes, first_elf, second_elf):
    """

    :param recipes:
    :param first_elf:
    :param second_elf:
    :return:
    """
    print("first elf: recipe {} at index {}, second elf: recipe {} at index {}, total number of recipes: {} recipes: {}".format(
            recipes[first_elf], first_elf,
            recipes[second_elf], second_elf, len(recipes),
            recipes))


if __name__ == "__main__":
    input = 9
    #input = 890691
    print(part1(input))

