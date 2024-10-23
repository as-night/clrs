'''Selection sort'''

__all__ = ['selection_sort']

from typing import List

def selection_sort(a: List[int]) -> None:
    index_of_min = 0
    for i in range(len(a)):
        index_of_min = i
        for j in range(i + 1, len(a)):
            if a[j] <= a[index_of_min]:
                index_of_min, j = j, index_of_min
        if a[index_of_min] <= a[i]:
            a[i], a[index_of_min] = a[index_of_min], a[i]

def main() -> None:
    l = [31, 41, 59, 26, 41, 58]
    print('Before sorting:', l)
    selection_sort(l)
    print('After sorting:', l)

if __name__ == '__main__':
    raise SystemExit(main())
