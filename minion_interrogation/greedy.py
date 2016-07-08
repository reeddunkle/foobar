from __future__ import division

def answer(minions):
    '''
    Given a list of minions, each minion as a list of characteristics,
    returns the lexographically smallest ordering of the minions according
    to the smallest expected time required in the machine.
    '''

    sortkey = [time/(num/denom) for time, num, denom in minions]

    return sorted(range(len(minions)), key=lambda i: sortkey[i])
