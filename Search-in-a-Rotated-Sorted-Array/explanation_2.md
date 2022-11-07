"""
Explanation of;
Project: Problems vs Algorithms
Problem 2: Search in a Rotated Sorted Array
"""

#I created some helper functions. These are;

#binary_search() --> This is a standart binary search

#find_pivot() --> This function finds the pivot elements index in the given rotated array. 
#Which's runtime is O(logn).

#rotated_array_search() --> Finds the pivot elements index 
#and do determines two arrays as left and right

#ex: [4,5,6,7,1,2,3] 
#left part is [4,5,6,7] right part is [1,2,3]
#and chooses the left or right array acording to the target elemet that we want to find of index
#than perfoms the binary_search function to selected part.

#runtime complexity is O(logn)
#space complexity is O(n) because we take n size array.