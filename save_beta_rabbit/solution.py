'''
    Save Beta Rabbit:
    -----------------

    To be freed, Beta Rabbit needs to make his way to the bottom right room
    (which also has a hungry zombie) and have used most of the limited food
    he has. He decides to take the path through the grid such that he ends up
    with as little food as possible at the end.
'''


def min_positive(a, b):
    '''Given a and b, returns the min(a,b) if they are both positive,
    returns the max(a,b) if at least one is negative.
    '''
    return min(a, b) if a >= 0 and b >= 0 else max(a, b)


def spend_most_food(food, grid, dest_r, dest_c):

    memoizers = set([])
    stack = []
    stack.append((0, 0, food))

    best = -1

    while len(stack) > 0:
        node = stack.pop()

        if node not in memoizers:
            memoizers.add(node)
            r, c, food = node

            if food < 0:
                continue

            if r < dest_r:
                stack.append((r+1, c, food-grid[r+1][c]))
            if c < dest_c:
                stack.append((r, c+1, food-grid[r][c+1]))

            if r == dest_r and c == dest_c:
                best = min_positive(best, food)

    return best


def answer(food, grid):
    '''Given food quantity and the grid, returns the number of units of
    food left after taking a route using up as much food as possible while
    still ending at the bottom right room. If there is not enough food for
    any route, returns -1.
    '''
    dest_r = len(grid)-1
    dest_c = len(grid[0])-1
    return spend_most_food(food, grid, dest_r, dest_c)
