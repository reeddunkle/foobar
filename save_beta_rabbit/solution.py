'''
    Save Beta Rabbit:
    -----------------

    To be freed, Beta Rabbit needs to make his way to the bottom right room,
    feeding each room's zombie the food it requires for safe passage, using
    the limited food he has. He decides to take the path through the grid
    such that he ends up with as little food as possible at the end.
'''


from collections import namedtuple

PathStep = namedtuple('PathStep', ['row', 'col', 'food_left'])


def best_result(food1, food2):
    '''If both food1, food2 are non-negative return the minimum,
    if at least one is negative return the maximum.
    '''
    return min(food1, food2) if food1 >= 0 and food2 >= 0 else max(food1, food2)


def step_down(step, grid):
    '''Return the result of moving down one step in the grid.'''
    return PathStep(step.row + 1, step.col,
           step.food_left - grid[step.row + 1][step.col])


def step_right(step, grid):
    '''Return the result of moving right one step in the grid.'''
    return PathStep(step.row, step.col + 1,
           step.food_left - grid[step.row][step.col + 1])


def spend_most_food(starting_food, grid):
    '''Calculate which path from the top left to the bottom right in
    the grid will spend the most food along the way without running out.
    Beta Rabbit can only move down and right. Return the amount of leftover
    food, or -1 if there is not enough food to reach the destination.
    '''
    cache = set([])
    last_row = len(grid) - 1
    last_col = len(grid[0]) - 1
    best = -1

    steps_to_take = [PathStep(0, 0, starting_food)]
    while len(steps_to_take) > 0:
        head = steps_to_take.pop()

        if head not in cache:
            cache.add(head)

            if head.food_left < 0:
                continue

            if head.row < last_row:
                steps_to_take.append(step_down(head, grid))
            if head.col < last_col:
                steps_to_take.append(step_right(head, grid))

            if head.row == last_row and head.col == last_col:
                best = best_result(best, head.food_left)

    return best


def answer(starting_food, grid):
    '''Given food quantity and the grid, returns the number of units of
    food left after taking a route using up as much food as possible while
    still ending at the bottom right room. If there is not enough food for
    any route, returns -1.
    '''
    return spend_most_food(starting_food, grid)
