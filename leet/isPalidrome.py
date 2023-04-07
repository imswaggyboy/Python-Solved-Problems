class Solution(object):
    def isPalindrome(self, x):
#       at the start we'll check if the x is lessthen 0 if it is then not palidrome
        if x<0:
            return False
        else:
#           copy the x
            temp = x
#   create variable to add the reversed number
            reversed_number = 0 
#   iterate till the temp is greater than zero
            while temp >0:
#     extract the last digit with mod
                last_digit = temp%10
#   append it to reversed_number 
                reversed_number = reversed_number*10+last_digit
#   remove the last digit of temp
                temp = temp//10
#   check and return if the x == reversed_number
            return x == reversed_number
