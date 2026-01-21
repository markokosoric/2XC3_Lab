import bad_sorts;
import copy;
import math
import random
import timeit
import gc
import time
import matplotlib.pyplot as plt
from typing import Iterable, Tuple, Dict

class Bench:
    def __init__(self, sort) -> None:
        self.sort = sort

    def bench(self, L: list[int], n: int) -> float:
        total = 0;
        for i in range(n):
            l = copy.deepcopy(L);
            start = timeit.default_timer();
            self.sort(l);
            elapsed = timeit.default_timer() - start;
            total += elapsed
        return total/float(n);

def bench_algo(sort, lengths: list[int], max_val: int, n: int) -> list[int]:
    data = [];
    bench = Bench(sort);
    for size in lengths:
        L = bad_sorts.create_random_list(size, max_val)
        time = bench.bench(L, n)
        data.append(time);
    return data;

def exp1():
    lengths = [
        100,
        200,
        300,
        400,
        500,
        600,
        700,
        800,
        900,
        1000,
        1100,
        1200,
        1300,
        1400,
        1500,
        1600,
        1700,
        1800,
        1900,
    ];
    i_data = bench_algo(bad_sorts.insertion_sort, lengths, 2000000, 10);
    s_data = bench_algo(bad_sorts.selection_sort, lengths, 2000000, 10);
    b_data = bench_algo(bad_sorts.bubble_sort, lengths, 2000000, 10);

    print("insertion: ", i_data);
    print("selection: ", s_data);
    print("bubble: ", b_data);
    plt.plot(lengths, i_data, color='red')
    plt.plot(lengths, s_data, color='green')
    plt.plot(lengths, b_data, color='blue')
    plt.legend(['insertion_sort', 'selection_sort', 'bubble_sort'])

    plt.xlabel('size')
    plt.ylabel('time (s)')

    plt.show()

