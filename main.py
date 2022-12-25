import concurrent.futures
import time

from read_file import read_file_to_array
from count_islands import Array, CountIslands

start = time.perf_counter()

array = read_file_to_array()
if __name__ == "__main__":
    if array:
        a = Array(array)
        islands = CountIslands(a)
        with concurrent.futures.ProcessPoolExecutor() as executor:
            ret = executor.submit(islands.count_islands)

        print(f"Number of islands: {ret.result()}")

    finish = time.perf_counter()

    print(f"Finished in {finish-start} seconds")
