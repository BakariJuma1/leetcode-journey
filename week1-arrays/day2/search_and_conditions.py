def search(List,n):
    for i in range(len(List)):
        if List[i] == n:
            return True
    return False        

 
List= (1,2,3,'boy',8)

n= 'boy'
if search(List,n):
    print(f'{n} found')
else:
    print(f"{n} not found ") 


def find_me(students,n):
    for i in range(len(students)):
        if students[i] == n:
            return True
    return False
    
students =('juma','ken',4,6,'g')
n='ken'

if find_me(students,n):
    print('student is in class')
else:
    print('student not in class')    

# using if statements in loops to add logic

def count_appearance(numbers,target):
    count = 0
    for i in numbers:
        if i == target:
            count += 1
    return count

print(count_appearance([1,2,3,4,5,5,8],5))        