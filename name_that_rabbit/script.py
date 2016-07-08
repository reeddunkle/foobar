import string

LETTERS = string.ascii_lowercase
LETTER_SCORES = {}

for i, letter in enumerate(LETTERS):
    LETTER_SCORES[letter] = i + 1


def score(s):
    '''
    Given string, returns integer representing that
    string's total letter-value. (a=1, b=2...z=26)
    '''

    return sum([LETTER_SCORES[letter] for letter in s])


def answer(names):
    '''
    Given a list of names, returns the list sorted in descending
    order based on their score. (All names are lowercase.)
    '''

    result = sorted(names)
    result = sorted(result, key=lambda name: score(name))

    return list(reversed(result))
