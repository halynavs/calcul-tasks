import time
import numpy as np
from solution_task_2 import islands_count


np.random.seed(4)
matrix1 = [[0,  1,  0],
          [0,  0,  0],
          [0, 1, 1]]
matrix2 = [[0,  0,  0,  1],
          [0,  0,  1,  0],
          [0, 1, 0, 0]]
matrix3 = [[0,  0,  0,  1],
          [0,  0,  1,  1],
          [0, 1, 0, 1]]

# matrix = np.random.randint(2, size=(10**2,10**2)) #


time1 = time.time()
print(np.array(matrix1))
print('The number of islands:', islands_count( matrix1))
print("Execution time --- %s seconds ---" % (time.time() - time1))

time2 = time.time()
print(np.array(matrix2))
print('The number of islands:', islands_count( matrix2))
print("Execution time --- %s seconds ---" % (time.time() - time2))

time3 = time.time()
print(np.array(matrix3))
print('The number of islands:', islands_count( matrix3))
print("Execution time --- %s seconds ---" % (time.time() - time3))













# time1 = time.time()
# print(matrix.sum())
#
# print("--- %s seconds ---" % (time.time() - time1))

# time2 = time.time()
# import tensorflow as tf
# print(tf.math.reduce_sum(
#     matrix, axis=None, keepdims=False, name=None
# ))
# print("--- %s seconds ---" % (time.time() - time2))

# # binary search within each row for O(nlogm) runtime
# from bisect import bisect_left
#
# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix or not matrix[0]:
#             return False
#         for row in matrix:
#             i = bisect_left(row, target)
#             if i < len(row) and row[i] == target:
#                 return True
#         return False
# # matrix = [[ 0,  1,  2,  3,  4,  5],
# #           [ 6,  7,  8,  9, 10, 11],
# #           [12, 13, 14, 15, 16, 17],
# #           [18, 19, 20, 21, 22, 23],
# #           [24, 25, 26, 27, 28, 29]]
# # target = 10
# matrix = matrix.tolist()
# print(type(matrix))
# S = Solution()
# print(S.searchMatrix(matrix, 1))
#
# # using naive method
# # to get numbers > k
# count = 0
# count = sum([i == 1  for i in line.split()]for i in matrix)
#
# # printing the intersection
# print("The numbers ==1: " + str(count))