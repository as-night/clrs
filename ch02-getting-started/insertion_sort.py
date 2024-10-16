import sys
from typing import List

'''Insertion sort

For simplicity's sake, the sorting algorithm is constrained to work
with lists of strings only - for now.

Due to Python's limitations, namely immutability of strings, the
algorithm requires to map the individual characters/strings coming
from the standard input to ints, assigning them into a new list in the
process. This makes for O(len(list_to_sort)) space complexity.

The time complexity is O(len(list_to_sort)), just as in the original
version of the algorithm.
'''

__all__ = ['insertion_sort']
__author__ = ['as-night']

# The provisional List[str] simplifies initial testing of the code.
# Passing args on the command line while running the script is easier
# than constant retyping (or commenting out) of different lists
# directly in the source code.
#
# Definetely something to fix when the implementation is finally
# correct.
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
