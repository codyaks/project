import array as arr
#set data type
numset=set([1,2,3,4,6])
print(numset)
numset.pop()
print(numset)

lst=[1,2,4,6,1]
print(lst)
set1=set(lst)
print(set1)

print(" ")
set1={1,2,4}
set2={4,5,6}
print(set1)
print(set2)
set_union=set1.union(set2)
print(set_union)
setin=set1.intersection(set2)
print(setin)

#array
num_array=arr.array("i",[1,2,3,4,5,3,3])
print(num_array)
print(num_array.count(3))
num_array.reverse()
print(num_array)