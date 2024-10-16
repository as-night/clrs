import time
import timeit

SETUP = '''
import random
a = [str(random.randint(0, 1_000_000)) for _ in range(1_000_001)]
'''

MAP = '''
b = []
b = list(map(int, a))
'''

LIST_COMP = '''
b = []
b = [int(_) for _ in a]
'''
# TODO: Find out why it doesn't work as expected, i.e., it generates
# a list of which each member is a map object, instead of list of
# numbers.
# MAP_BRACKET = '''
# b = []
# b = [map(int, a)]
# print(b)
# '''

def main():
    t = timeit.timeit(stmt=MAP,
                      setup=SETUP,
                      timer=time.perf_counter_ns,
                      number=100)
    print(f'map took: {t / 1_000_000_000} second(s) of time.')

    t = timeit.timeit(stmt=LIST_COMP,
                      setup=SETUP,
                      timer=time.perf_counter_ns,
                      number=100)
    print(f'list comp took: {t / 1_000_000_000} second(s) of time.')

    # t = timeit.timeit(stmt=MAP_BRACKET,
    #                   setup=SETUP,
    #                   timer=time.perf_counter_ns,
    #                   number=100)
    # print(f'list comp took: {t / 1_000_000_000} second(s) of time.')

if __name__ == '__main__':
    raise SystemExit(main())
