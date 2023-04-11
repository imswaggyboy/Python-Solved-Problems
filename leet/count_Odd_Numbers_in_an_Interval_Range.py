# 1523. Count Odd Numbers in an Interval Range

# ---------------------------------------------------------------------
# brute force approach
# time:O(n)
# ----------------------------------------------------------------------

class Solution(object):
    def countOdds(self, low, high):
        lst = []
        for num in range(low,high+1):
            if num%2!=0:
                lst.append(num)
        return len(lst)


# ---------------------------------------------------------------------
# jst a mathematics approach (guess what i dont i learnt from g4g) 
# time:O(1)
# ----------------------------------------------------------------------

class Solution(object):
    def countOdds(self, low, high):
        n = high-low+1
        if n%2==0:
            return n//2
        else:
            if high%2:
                return n//2+1
            else:
                return n//2
              
