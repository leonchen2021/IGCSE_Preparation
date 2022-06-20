Studentlist = ["Leon", "Mars", "Hason"]
Studentlist.append("David")
print(Studentlist)

#%%
#order the list

Rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(0,7):
    print(i, Rainbow[i])

#%%
#append the value into the list
Rainbow = []
HowMany = input("How many elements in the list ")
HowMany = int(HowMany)

for i in range(0,HowMany):
    NewValue = input("enter the next element of the list: ")
    Rainbow.append(NewValue)

#%%
my_list = [10,11,12,13,14]
i = [1,4]
element = []
for index in i:
    element.append(my_list[index])
print(element)