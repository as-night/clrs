'''Linear search

A simple, proof-of-concept implementation of linear search.
'''

__all__ = ['linear_search']

from typing import List, Optional

# We're running on macOS' 3.9.6 by default, so no support for the |
# operator in function signatures.
def linear_search(a: List[int], key: int) -> Optional[int]:
    '''Return the index of the first occcurence of a key or None.'''
    for index, value in enumerate(a):
        if value == key:
            return index
    return None

def main() -> None:
    l = [31, 41, 59, 26, 41, 58]
    key = 22
    print(f'list: {l}',
          f'key: {key}',
          sep='\n')
    ret = linear_search(l, key)
    if ret:
        print(f'Found the key {key} at the index {ret}.')
    else:
        print(f'Found {ret}.')

if __name__ == '__main__':
    raise SystemExit(main())
