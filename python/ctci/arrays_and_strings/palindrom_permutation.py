import collections

def palin_perm(input):
    if input is None or len(input) == 0:
        return False
    table = collections.defaultdict(int)
    for c in input:
        if c != ' ':
            table[c] += 1

    odd = 0
    for _, val in table.items():
        if val & 1 == 1:
            odd += 1
        if odd > 1:
            return False
    return True

if __name__ == '__main__':
    test = 'tact coa'
    print(palin_perm(test))

    test = 'tactcoa'
    print(palin_perm(test))

    test = 'tactco'
    print(palin_perm(test))

    test = 'tctc'
    print(palin_perm(test))

    test = ''
    print(palin_perm(test))

    test = 'tactcoapapa'
    print(palin_perm(test))