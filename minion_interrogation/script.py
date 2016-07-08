from __future__ import division
from itertools import permutations


def estimated_time(index_list, minions):
    '''
    Given a list of indices, calculates and returns
    the estimated time for that order of minions.
    '''

    cur_time = 0
    cummulative_failure = 1
    total_time = 0

    for i in index_list[:-1]:
        time, num, denom = minions[i]

        cur_time += time
        cur_success = num / denom

        total_time += cur_time * cummulative_failure * cur_success

        cur_failure = 1 - cur_success
        cummulative_failure *= cur_failure

    time, num, denom = minions[index_list[-1]]
    cur_time += time
    cur_success = num / denom
    total_time += cur_time * cummulative_failure

    return total_time


def answer(minions):
    '''
    Given a list of minions, each minion as a list of characteristics,
    returns the lexographically smallest ordering of the minions according
    to the smallest expected time required in the machine.
    '''

    index_perms = permutations(range(len(minions)), len(minions))

    best_time = None
    best_index_perm = None

    for perm in index_perms:
        # minion_list = [minions[i] for i in perm]
        score = estimated_time(perm, minions)

        if best_time is None:
            best_time = score
            best_index_perm = perm

        elif score < best_time:
            best_time = score
            best_index_perm = perm

    return list(best_index_perm)
