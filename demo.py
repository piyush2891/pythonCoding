my_list = ["jan", "feb", "mar"]
#print(my_list[1])
for val in my_list:
    print(val)

my_list.append("april")
my_list.append("april")
print(my_list)

my_set = set(my_list)
print(my_set)

new_set = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}
for valu in new_set:
    print(valu)
#print(new_set[2])  will give error as we can't access the values of set
new_set.add("jan")
print(new_set)
new_set.remove("mon")
print(new_set)
# in set order will change on every execution
# add and remove function will work for set
# append and remove function will work for list
# dictionary {"days" : 20, "units" : "minutes"}



"""list uses [] and set uses {}"""
# sets are unordered and unchangeable
# items in a set can't be referred using their index
# items can't be changed only can be removed/added

