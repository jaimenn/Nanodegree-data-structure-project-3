"""
Explanation of;
Project: Problems vs Algorithms
Problem 1: Square Root of an Integer
"""

#I begin while looking for the middle element of number
#and compare mid's square(mid**2) with number
#
#if it is bigger than number middle element becomes up edge of the range
#if it is lower than number middle element becomes down edge of the range
#
#the calculate the middle again and range that 
#we are looking f#or sqrt is getting smaller
#
#range is always tuns into it's half
#
#
#So;
#time complexity is O(logn)
#
#also;
#space comlexity is O(logn)