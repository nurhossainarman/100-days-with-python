def removeDuplicates(list):
    newlist = []
    for num in list:
        if num not in newlist:
            newlist.append(num)
    return newlist

size = input("Enter the size of your list:")
userList = []
print("Insert values:")
for i in range(int(size)):
    userList.append(int(input()))
print(f"Here is your new list: {removeDuplicates(userList)}")