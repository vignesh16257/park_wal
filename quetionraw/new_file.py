list=[1,2,3,4,1,2,3,4]
list_2=[1,2,5,6]

new_list=[]

for i in list:
    if i not in new_list:
        new_list.append(i)

print(new_list)