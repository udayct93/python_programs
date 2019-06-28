import re
f=open("C:/Users/adminlocal/Downloads/duplicate.txt","r" )
ilist =[]
for x in f:
    if x not in ilist:
        ilist.append(x)
# print(ilist)

lt = []
for x in ilist:
    if x.strip().startswith("Event"):
        for y in eval(x.strip("Event : "))["Records"]:
            z = y["s3"]["object"]["key"]
            lt.append(z)


print(lt)



# dup_list=[]
# for i in range(len(lt)-1):
#     if(lt.count(lt[i])>1):
#         dup_list.append(lt[i])
#         print(dup_list)
#
#
# for num in lt:
#     lt2 = set(lt)
#     lt3 = []
#     lt2.add(num)
#     for  p in lt:
#         if p not in lt2:
#             lt3.append(y)
#
# print(lt3)

s_list=lt
for i in range(len(s_list) - 1):
    if s_list[i] == s_list[i + 1]:
        if s_list[i] not in lt:
            lt.append(s_list[i])
print(s_list)

