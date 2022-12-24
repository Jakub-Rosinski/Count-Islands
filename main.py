from read_file import read_file_to_array
from count_islands import Array, CountIslands

array = read_file_to_array()

a = Array(array)
islands = CountIslands(a)
print(islands.count_islands())
