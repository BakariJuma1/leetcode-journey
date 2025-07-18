# Problem1:
# Write a function called count_occurrences that takes in:
# a list of items, and
# a target value x.
# It should return how many times x appears in the list.

def count_occurences(List,x):
    count = 0
    for i in range(len(List)):
        if List[i] ==x:
            count +=1
    return count       

print(count_occurences([2,3,3,4,5],3))

# Problem2
# Write a function called find_max that takes in a list of numbers and returns the largest number in the list.
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num >max_num:
            max_num = num
    return max_num
print(find_max(numbers=(1,2,3,4,5,6,78,9)))

# Problem 3
# Write a function called get_evens that:
# Takes in a list of numbers
# Returns a new list containing only the even numbers

def get_evens(nums):
    even_nums =[]
    for i in range(len(nums)):
        if nums[i]%2 ==0:
            even_nums.append(nums[i])
    return even_nums

print(get_evens(nums=(1,2,3,4,5,5,6,7)))        

# Problem
# Write a function called find_index_of that:
# Takes in a list and a target value x
# Returns the index of the first time x appears
# If it’s not found, return -1

def find_index(my_num,x):
    for i in range(len(my_num)):
        if my_num[i] == x:
            return i
        
    return -1   
print(find_index([2,3,4,4,5,6,7],4))
                