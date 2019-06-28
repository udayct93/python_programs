# x_list = [1, 3, 7, 8, 5, 7, 8, 3, 8, 10]
#
# list1=(list(dict.fromkeys(x_list)))
# print(list1)
# list2=[]
# for i in range(len(x_list)):
#     if (x_list.count(x_list[i]>1)):
#         list2.append(x_list[i])
# print(list2)

my_list = [1, 3, 7, 8, 5, 7, 8, 3, 8, 10]

list2=(list(dict.fromkeys(my_list)))

new_list = sorted(set(my_list))
print(my_list)
print(list2)
dup_list = []

for i in range(len(new_list)):
    if (my_list.count(new_list[i]) > 1):
        dup_list.append(new_list[i])

print(dup_list)





# duplicate remove : list_1

# list duplicate value : list_2
