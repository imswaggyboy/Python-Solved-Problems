# Use for the questions below:
nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

# 1. Find all of the numbers from 1–1000 that are divisible by 8
q1_answer = [num for num in nums if num % 8 == 0]

# 2. Find all of the numbers from 1–1000 that have a 6 in them
q2_answer = [num for num in nums if "6" in str(num)]

# 3. Count the number of spaces in a string
q3_answer = len([char for char in string if char == " "])

#4. Remove all of the vowels in a string
q4_answer = "".join([char for char in string if char not in ["a","e","i","o","u"]])
