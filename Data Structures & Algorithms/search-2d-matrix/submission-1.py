# non-decreasing as in ascending order with duplicates
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow():
            top = 0
            bottom = len(matrix) - 1

            while top <= bottom:
                middle = (top+bottom)//2
                # first represents the very first element in the middle row of the matrix
                first = matrix[middle][0]
                # Last represents the last element in the middle row of the matrix
                last = matrix[middle][-1]

                # we move the bottom (last row) to middle - 1
                if target < first:
                    bottom = middle - 1
                # we move the top (first row) to middle + 1
                elif target > last:
                    top = middle + 1
                # target is in range of this row
                else:
                    return middle
            return -1

        targetRow = findRow()
        # keep in mind that we cant do r = len(matrix[targetRow]) - 1
        # if targetRow is -1 (its supposed to be invalid), it indexes
        # to the last index and then subtracts 1

        if targetRow == -1:
            return False
        
        # implement second binary search

        l = 0
        r = len(matrix[targetRow]) - 1

        while (l <= r):
            middle = (l+r)//2
            if target < matrix[targetRow][middle]:
                r = middle - 1
            elif target > matrix[targetRow][middle]:
                l = middle + 1
            else:
                return True
        return False









# brainstorm
# can use first element in the row to quickly search and use it
# to compare with the target

# what i am thinking is we find the row the target may be in using the first element. Then we can just search within that row to see if the target is in there or not. 

# matrix[i][0] first element in i row. Gather the number of rows -> top row = 0, bottom row = last, middle = (top+bottom)//2. 
# We then search from middle and compare as you would for binary search.

# trying to figure out the conditional statements
# say you have target=13. You will find that 10 is less than 13, but 13 could be in that row with 10. 13 is also less than 14, so it's probably in that row.
# What im getting at is that target < row above, but target could be > than the first element in that row. 

# double binary search, do the same in that selected row.

# in a selected row, how do we access the last element?

# tldr binary search the column (first element), then binary search within the row.




# lost in the sauce

# targetRow = 0
    # # binary search to find the row we want
    # def findRow():
    #     top = 0
    #     bottom = len(matrix) - 1        
    #     while (top <= bottom):
    #         middle = (top+bottom)//2

    #         if target == matrix[middle]:
    #             return middle

    #         if target < matrix[middle]:
    #             bottom = middle - 1
            
    #         if target > matrix[middle]:
    #             top = middle + 1
    #         targetRow = middle
    #     return - 1
    

    # print(targetRow)
    # def findinRow():
    #     # binary search in that row to get the time complexity
    #     l = 0
    #     r = len(matrix[targetrow]) - 1
    #     while (l <= r):
    #         middle = (l+r)//2
    #         if target == middle:
    #             return True
    #         if target < middle:
    #             r = middle -1
    #         if target > middle:
    #             l = middle + 1
    #         return 

    # return False
