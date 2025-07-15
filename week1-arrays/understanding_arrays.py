# an array is a data structure that will allow you to store more than one value at a time
# list can contain mixed type of items,lists can store duplicates ,mutable and ordered 
# order is maintained by how items are added 
# access the items using index
students = ['brian','kamau','winnie','juma']
# accesing items in a list 
print(students[0])
# list with different data type 
data = [4,'six',True]
print(data[1])
# list with repeted items 
a =[3]*4
print(a)
# adding elemets to a list use either append(one element to the end of the list),extend(adds multiple elements to the end ),insert(add an element at a specific position)


subjects=['math']
subjects.append('chemistry')
subjects.extend(['geography','kiswahili'])
subjects.insert(1,'HELLO')
print(subjects)

# removing elements
# you can use remove(removes the first element),pop(removes the las or any at index if provided),del statement(specific index)
# fr remove you have to speccify what to remove it does not explicitly remove the first element while pop you use index
programming_languages=['python','c++','java','javascript','c#']
programming_languages.remove('c++')
programming_languages.pop(0)
# print(programming_languages)

# iterating
for language in programming_languages:
    print(language)

    #using for loop with range 


shopping=['soap','sugar','salt']
b=len(shopping)
for item in range(b):
    if item == 2:
       print(shopping[1])
    break  

b = [1,4,5,6]
for i in range(len(b)):
    if i == 0:
        print(b[0])
# enumarate  provides both the index and the value of each element during the loop
z= [1,3,4,5,6,8]
for i ,val in enumerate (z):
   print(val)
print("---------------------------------------")
# x =len(z)
for num in range(len(z)):
    print('second')
    print(num)
print("---------------------------------------")
a = [1,2,3,4,5,6] 
n=len(a)
for num in range(n):
    print(num)      
# lists start from 0     # 
