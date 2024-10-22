'''Insertion sort

For now, in order to facilitate the ease of testing via the command
line, the sorting algorithm takes as the input a list of strings.

Since Python's strings are immutable, the algorithm requires an
auxillary list to hold the conversion results (list[str] -> list[int]).
That makes the space complexity to become O(len(list_to_sort)).

The time complexity is O(len(list_to_sort)), just as in the original
version of the algorithm.
'''

__all__ = ['insertion_sort']

import sys
from typing import List

def insertion_sort(a: List[str]) -> List[int]:
    a = list(map(int, a))

    i = key = 1
    for j in range(1, len(a)):
        i = j - 1
        key = a[j]
        while i >= 0 and key < a[i]:
            a[i], a[j] = a[j], a[i]
            i -= 1
            j -= 1

    return a

def main(a: List[str]):
    print('Before sorting:', a,
          'After sorting:', insertion_sort(a),
          sep='\n')

# To run the script, pass all the integers to be sorted,
# space-separated, on the command line.
if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        raise SystemExit('No arguments given. Done.')
    raise SystemExit(main(args))
