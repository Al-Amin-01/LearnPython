lucky_numbers=[4,8,7,12]
friends=["karen","kevin","Jim","oscar","alice","bob"]
#add another friend at the end
friends.append("creed")
print(friends)

#add an element inside the list

friends.insert(1,"jibon")
print(friends)

#insert a list
friends.extend(lucky_numbers)
print(friends)
print(friends[-4:])