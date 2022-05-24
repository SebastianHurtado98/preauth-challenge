# Problem constraints
number_of_tests = 100
upper_bound = 10000
lower_bound = 1

import random

def generate_array(n=10):
    new_array = []
    for _ in range(n):
        new_array.append(random.randint(lower_bound, upper_bound))
    return new_array

# Brute force approach:
# Time complexity: O(n**2). Time will increase exponentially
# Space complexity: O(1). We will no require extra memory.

def brute_force_solution(M, N):
    for x in M:
        for y in M:
            if x + y == N:
                return [x, y]
    return []

# Binary search approach:
# Time complexity: O(nlogn). According to documentation, 
# Python built-in sort function has a O(nlogn). Binary search perform (at worst case)
# n times has a total complexity of O(logn), therefore, total complexity is O(nlogn).
# Space complexity: O(1). We will no require extra memory.

def binary_search(M, x):
    lower = 0
    upper = len(M) - 1
    pivot = 0
    while lower <= upper:
        pivot = (upper + lower) // 2
        if M[pivot] < x:
            lower = pivot + 1
        elif M[pivot] > x:
            upper = pivot - 1
        else:
            return True
    return False


def binary_search_solution(M, N):
    M.sort()
    for x in M:
        if binary_search(M, N - x):
            return [x, N - x]
    return []

def binary_search_solution_b(sorted_array, N):
    for x in sorted_array:
        if binary_search(sorted_array, N - x):
            return [x, N - x]
    return []


# Hash table approach:
# Time complexity: O(n). O(n) to build the table and O(n) 
# in worst case scenario to find the answer.
# Space complexity: O(n). We require extra space for the table. 


def build_hash_table(M):
    ht = dict()
    for x in M:
        ht[str(x)] = 1
    return ht

def hash_table_solution(M, N):
    ht = build_hash_table(M)
    for x in M:
        if str(N-x) in ht:
            return [x, N-x]
    return []

def hash_table_solution_b(ht, N):
    for x in ht:
        x_int = int(x)
        if str(N-x_int) in ht:
            return [x_int, N-x_int]
    return []

# Test: FIRST SCENARIO:
import time

def measure_function_time(func, M, y):
    start = time.time()
    func(M, y)
    end = time.time()
    return end - start

brute_force_time = 0
binary_search_time = 0
hash_table_time = 0

for i in range(number_of_tests):
    print("Test {}/{}".format(i, number_of_tests))
    M = generate_array(upper_bound)
    y = random.randint(lower_bound, upper_bound)
    brute_force_time += measure_function_time(brute_force_solution, M, y)
    binary_search_time += measure_function_time(binary_search_solution, M, y)
    hash_table_time += measure_function_time(hash_table_solution, M, y)

# Test: SECOND SCENARIO (multiple requests, low write, high read):
binary_search_many_requests_time = 0
hash_table_many_requests_time = 0

M = generate_array(upper_bound)

ht = build_hash_table(M)
sorted_array = sorted(M)

number_of_tests = 10000
for i in range(number_of_tests):
    print("Test {}/{}".format(i, number_of_tests))
    y = random.randint(lower_bound, upper_bound)
    binary_search_many_requests_time += measure_function_time(binary_search_solution_b, sorted_array, y)
    hash_table_many_requests_time += measure_function_time(hash_table_solution_b, ht, y)


# Answers

print("Brute force time: ", brute_force_time)
print("Binary search time: ", binary_search_time)
print("Hash table time: ", hash_table_time)

print("Binary search many requests: ", binary_search_many_requests_time)
print("Hash table many requests: ", hash_table_many_requests_time)


# Conclusion:
# For most cases the binary search approach is the best one (despite the theorical analysis).
# However, in the second scenario we can take advantage of the O(1) find operation in the hash table.