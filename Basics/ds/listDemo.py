# indexed based, allow duplicates
list1 = [20,34,87,23,34,35,1,2,3,4,5]
print(list1)
print(f"list[1:3]: {list1[1:3]}")
print("No. of Elements: ",len(list1))
#slice() mainly takes three parameters which have the same meaning in both constructs:
#start - starting integer where the slicing of the object starts
#stop - integer until which the slicing takes place. The slicing stops at index stop - 1.
#step - integer value which determines the increment between each index for slicing
#If a single parameter is passed, start and step are set to None.
#If two parameter passed, step is set to None
print(f"list[1:3]: {list1[slice(1,len(list1),3)]}")

