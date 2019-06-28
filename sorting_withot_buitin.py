# list1=[1,3,2,4,-6,5,8,7,10,9]
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)
#
#



mylist = [2, 1, 3, 4, 4, 4, 5, 5, 3]
s_list = sorted(mylist)
lt = []
for i in range(len(s_list) - 1):
    if s_list[i] == s_list[i + 1]:
        if s_list[i] not in lt:
            lt.append(s_list[i])
print(lt)
