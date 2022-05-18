from algorithms.sort import merge_sort
from algorithms.sort import bubble_sort
from algorithms.sort import bucket_sort
from algorithms.sort import cocktail_shaker_sort
from algorithms.sort import comb_sort
from algorithms.sort import counting_sort
from algorithms.sort import cycle_sort
from algorithms.sort import max_heap_sort
from algorithms.sort import insertion_sort
from algorithms.sort import pancake_sort
from algorithms.sort import pigeonhole_sort
from algorithms.sort import quick_sort
from algorithms.sort import radix_sort
from algorithms.sort import selection_sort
from algorithms.sort import shell_sort
from time import process_time

def sort(arr):
    return shell_sort(arr)

import random

file_object = open('sort_performance_list.txt', 'a')
file_object.write("shell_sort;")

my_list = []

for i in range (100):
    my_list.append(random.randint(0, 10000))

start = process_time()
my_list = sort(my_list)
stop = process_time()

print(stop - start)
file_object.write(str(stop - start))
file_object.write(";")

my_list = []

for i in range (1000):
    my_list.append(random.randint(0, 10000))

start = process_time()
my_list = sort(my_list)
stop = process_time()

print(stop - start)
file_object.write(str(stop - start))
file_object.write(";")

my_list = []

for i in range (10000):
    my_list.append(random.randint(0, 10000))

start = process_time()
my_list = sort(my_list)
stop = process_time()

print(stop - start)
file_object.write(str(stop - start))
file_object.write(";")

my_list = []

for i in range (100000):
    my_list.append(random.randint(0, 10000))

start = process_time()
my_list = sort(my_list)
stop = process_time()

print(stop - start)
file_object.write(str(stop - start))
file_object.write(";")

my_list = []

for i in range (1000000):
    my_list.append(random.randint(0, 10000))

start = process_time()
my_list = sort(my_list)
stop = process_time()

print(stop - start)
file_object.write(str(stop - start))
file_object.write(";")

file_object.write("\n")

file_object.close()