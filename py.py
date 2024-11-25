my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(2, 15)
my_listb = [50, 60, 70]
my_list.extend(my_listb)
remove = my_list.remove(70)
my_list.sort()
ind=my_list.index(30)
print("my list after sorting:", my_list)
print("The index of 30 is:", ind)