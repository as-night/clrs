import sys
from typing import List

'''Insertion sort

For simplicity's sake, the sorting algorithm is constrained to work
with lists of integers only - for now.

The sorting creates a new list of items every time it needs to move
the key into its designated spot, i.e., the sorting is not in place.
'''

def insertion_sort(a: List[str]) -> List[int]:
    a = list(map(int, a))
    if len(a) <= 1:
        return a
    if len(a) == 2:
        return [min(a), max(a)]

def main(a=[]):
    print('Before sorting:', a,
          'After sorting:', insertion_sort(a),
          sep='\n')

# To run the script, pass all the integers to be sorted on a command
# line, space separated.
if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        raise SystemExit('No arguments given. Done.')
    raise SystemExit(main(args))
