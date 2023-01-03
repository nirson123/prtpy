import math
import random
import time
from typing import List

import numpy as np

from simulations.recursive_number_partitioning_sy_v2_huristics_test import rnp
from prtpy.binners import BinnerKeepingContents
import matplotlib.pyplot as plt


def rnp_test_huristic(items, numbis: int, huristic_to_miss: int, n_tries: int = 1) -> float:
    """
    test the run time of rnp_v2 on the given parameters
    """
    huristics = [1, 2, 3, 4]
    if not huristic_to_miss == -1:
        huristics.remove(huristic_to_miss)

    total_time = 0
    for _ in range(n_tries):
        start_time = time.time()
        rnp(BinnerKeepingContents(), numbis, items, huristics=huristics)
        total_time += time.time() - start_time

    return total_time / n_tries


def get_time_results(low:int, hight: int, numbins: int) -> List[List[float]]:
    """
    return an (4)X(high - low + 1) table of running times.
    the row is the heuristic that was not used (first row is all heuristics)
    the column is the number of items
    """
    times = [[], [], [], []]
    for n_items in range(low, hight + 1):
        print(f'{n_items=}')
        items = [random.randint(1, 30) for _ in range(n_items)]
        for i, huristic in enumerate([-1, 2, 3, 4]):
            times[i].append(rnp_test_huristic(items, numbins, huristic, 2))

    return times


def plot_times():
    """
    plot running times of rnp_v2 on different input sizes, removing one heuristic each time
    """
    low, high = 5, 20
    results = np.array(get_time_results(low, high, 3))
    plt.plot(range(low, high + 1), results[0] * 100, label='with all heuristics (X 100)')
    # plt.plot(range(low, high + 1), results[1], label='without (1)')
    plt.plot(range(low, high + 1), results[1], label='without (2)')
    plt.plot(range(low, high + 1), results[2], label='without (3)')
    plt.plot(range(low, high + 1), results[3], label='without (4)')

    plt.legend()
    plt.xlabel('number of items')
    plt.ylabel('time (log)')

    plt.yscale('log')

    plt.show()


if __name__ == '__main__':
    plot_times()





