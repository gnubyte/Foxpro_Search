# ############
# @Author: Patrick Hastings
# @Title: Utility Class
# @Purpose: Mostly search functions and simple algorithms to increase speed at scale
# @Date: 8-25-2017
# @Version: 0.1
# ############
# import sys # only import if setting recursion limit

class Utilities:
    '''
    A set of utility functions to increase performance at scale.
    '''
    def sanitizeInput(self, input):
        '''
        Cleans a string of any harmful strings
        '''
        dostuff = 'GET ER DONE'
    
    def BinarySearch(self, A, size, target):
        '''
        Runs a binary search on the parameters
        Recommended for more than ten params
        Requires sorted indexes/arrays
        A logarithm; the incrementor number of times we run the operation to get the target
        ------
        Best: floor(log2(n))+1
        Worst: ceil(log2(n)) +1
        Average Approx.: log2(n)+1
        '''
        low  = 0
        high = size
        while (low+1 <high):
            #while the low + 1 is less than the highest value
            test = (low+high)/2
            # our test number is the lowest and highest numbers added, split (get mid value)
            if (A[test] > target):
                #if the middle value of lowest and highest is greater than the target...
                high = test
                #set the new high to the test
            else:
                #otherwise our lowest is now the next test, start searching left of array
                low = test
        if (A[low] == target):
            return low
        else:
            return -1
    def LinearSearch(self, size, target):
        '''
        Checks for equality in individual elements procedurally
        Does not require sorted indexes
        '''