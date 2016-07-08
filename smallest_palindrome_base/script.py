import string


def int2base(x, base):
    '''
    Given integer and target base, returns that integer
    converted into target base.
    '''

    digs = string.digits + string.ascii_letters

    if x == 0:
        return digs[0]

    digits = []

    while x:
        digits.append(digs[x % base])
        x /= base

    return digits


def is_palindrome(s):
    '''
    Given string, returns boolean whether string is a palindrome.
    '''

    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False

    return True


def answer(n):
    '''
    Given integer, finds the smallest base into which the integer
    can be converted whose result is a palindrome.
    '''

    for base in range(2, 17):

        result = int2base(n, base)

        if is_palindrome(result):
            return base

    return -1


if __name__ == '__main__':

    x = int(raw_input())

    smallest_palindrome_base = answer(x)

    print(smallest_palindrome_base)
