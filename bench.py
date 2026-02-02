import bad_sorts;
import good_sorts;
import test_sort
import copy;
import math
import random
import timeit
import gc
import time
import matplotlib.pyplot as plt
from typing import Iterable, Tuple, Dict
import sys


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

def bench_algo2(sort, lengths: list[int], max_val: int, n: int) -> list[int]:
    data = [];
    bench = Bench(sort);
    for size in lengths:
        time = 0;
        for i in range(n):
            L = bad_sorts.create_random_list(size, max_val)
            time += bench.bench(L, 1)
        data.append(time/n);
    return data;


def bench_algo_almost_sorted(
        sort,
        length: int,
        max_val: int,
        swaps: list[int],
        n: int
) -> list[int]:
    data = [];
    bench = Bench(sort);
    for s in swaps:
        L = bad_sorts.create_near_sorted_list(length, max_val, s)
        time = bench.bench(L, n)
        data.append(time);
    return data;

def bench_algo_almost_sorted2(
        sort,
        length: int,
        max_val: int,
        swaps: list[int],
        n: int
) -> list[int]:
    data = [];
    bench = Bench(sort);
    for s in swaps:
        time = 0;
        for i in range(n):
            L = bad_sorts.create_near_sorted_list(length, max_val, s)
            time += bench.bench(L, 1)
        data.append(time/n);
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

def exp2_bubble():
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
    ]

    b_data_orig = bench_algo(bad_sorts.bubble_sort, lengths, 2000000, 10);
    b_data_opt = bench_algo(bad_sorts.bubble_sort2, lengths, 2000000, 10);
    print("normal bubble sort: ", b_data_orig);
    print("optimized bubble sort: ", b_data_opt);
    plt.plot(lengths, b_data_orig, color='red')
    plt.plot(lengths, b_data_opt, color='green')
    plt.legend(['normal bubble sort', 'optimized bubble sort'])

    plt.xlabel('size')
    plt.ylabel('time (s)')

    plt.show()

def exp2_selection():
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
    ]

    s_data_orig = bench_algo(bad_sorts.selection_sort, lengths, 2000000, 10);
    s_data_opt = bench_algo(bad_sorts.selection_sort2, lengths, 2000000, 10);
    print("normal selection sort: ", s_data_orig);
    print("optimized selection sort: ", s_data_opt);
    plt.plot(lengths, s_data_orig, color='red')
    plt.plot(lengths, s_data_opt, color='green')
    plt.legend(['normal selection sort', 'optimized selection sort'])

    plt.xlabel('size')
    plt.ylabel('time (s)')

    plt.show()

def exp3():
    length = 5000;
    swaps = [
        0,
        1000,
        2000,
        3000,
        4000,
        5000,
        6000,
        7000,
        8000,
        9000,
        10000,
    ];

    i_data = bench_algo_almost_sorted(bad_sorts.insertion_sort, length, 2000000, swaps, 10);
    s_data = bench_algo_almost_sorted(bad_sorts.selection_sort, length, 2000000, swaps, 10);
    b_data = bench_algo_almost_sorted(bad_sorts.bubble_sort, length, 2000000, swaps, 10);


    print("insertion: ", i_data);
    print("selection: ", s_data);
    print("bubble: ", b_data);
    plt.plot(swaps, i_data, color='red')
    plt.plot(swaps, s_data, color='green')
    plt.plot(swaps, b_data, color='blue')
    plt.legend(['insertion_sort', 'selection_sort', 'bubble_sort'])

    plt.xlabel('Number of swaps')
    plt.ylabel('time (s)')

    plt.show()

def exp4():
    lengths = [
        1000,
        2000,
        3000,
        4000,
        5000,
        6000,
        7000,
        8000,
        9000,
        10000,
        11000,
        12000,
        13000,
        14000,
        15000,
        16000,
        17000,
        18000,
        19000,
    ];
    q_data = bench_algo(good_sorts.quicksort, lengths, 2000000, 10);
    m_data = bench_algo(good_sorts.mergesort, lengths, 2000000, 10);
    h_data = bench_algo(good_sorts.heapsort, lengths, 2000000, 10);

    print("quicksort: ", q_data);
    print("mergesort: ", m_data);
    print("heapsort: ", h_data);
    plt.plot(lengths, q_data, color='red')
    plt.plot(lengths, m_data, color='green')
    plt.plot(lengths, h_data, color='blue')
    plt.legend(["quicksort", "mergesort", "heapsort"])

    plt.xlabel('size')
    plt.ylabel('time (s)')

    plt.show()

def exp5():
    sys.setrecursionlimit(10000)
    length = 2000;
    swaps = [
        0,
        1,
        2,
        4,
        8,
        16,
        32,
        64,
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
    ]

    q_data = bench_algo_almost_sorted2(good_sorts.quicksort, length, 2000000, swaps, 100);
    m_data = bench_algo_almost_sorted2(good_sorts.mergesort, length, 2000000, swaps, 100);
    h_data = bench_algo_almost_sorted2(good_sorts.heapsort, length, 2000000, swaps, 100);


    print("quicksort: ", q_data);
    print("mergesort: ", m_data);
    print("heapsort: ", h_data);
    plt.plot(swaps, q_data, color='red')
    plt.plot(swaps, m_data, color='green')
    plt.plot(swaps, h_data, color='blue')
    plt.legend(['quick_sort', 'merge_sort', 'heap_sort'])

    plt.xlabel('Number of swaps')
    plt.ylabel('time (s)')

    plt.show()

def exp6():
    lengths = [
        100,
        1000,
        2000,
        5000,
        10000,
        20000,
        30000,
        40000,
        80000,
        160000,
        200000,
        500000
    ]

    q_data = bench_algo(good_sorts.quicksort, lengths, 2000000, 10);
    dq_data = bench_algo(good_sorts.dual_quicksort, lengths, 2000000, 10);
    print("normal quick sort: ", q_data);
    print("dual quick sort: ", dq_data);
    plt.plot(lengths, q_data, color='red')
    plt.plot(lengths, dq_data, color='green')
    plt.legend(['normal quick sort', 'dual quick sort'])

    plt.xlabel('size')
    plt.ylabel('time (s)')

    plt.show()

def exp7():
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
        2000,
        3000,
        4000,
        5000,
        6000,
        7000,
        8000,
        9000,
        10000,
    ]

    m_data_rec = bench_algo2(good_sorts.mergesort, lengths, 2000000, 100);
    m_data_iter = bench_algo2(good_sorts.mergesort2, lengths, 2000000, 100);
    print("recursive merge sort:", m_data_rec);
    print("iterative merge sort:", m_data_iter);
    plt.plot(lengths, m_data_rec, color='red')
    plt.plot(lengths, m_data_iter, color='green')
    plt.legend(['recursive merge sort', 'iterative merge sort'])


def exp8():
    lengths = [
        i for i in range(41)
    ]

    q_data = bench_algo2(good_sorts.quicksort, lengths, 2000000, 10000);
    m_data = bench_algo2(good_sorts.mergesort, lengths, 2000000, 10000);
    i_data = bench_algo2(bad_sorts.insertion_sort, lengths, 2000000, 10000);

    print("quick sort: ", q_data);
    print("merge sort: ", m_data);
    print("insertion sort: ", i_data);

    plt.plot(lengths, q_data, color='red')
    plt.plot(lengths, m_data, color='green')
    plt.plot(lengths, i_data, color='blue')
    plt.legend(['quick sort', 'merge sort', "insertion sort"])

    plt.xlabel('size')
    plt.ylabel('time (s)')

    plt.show()
