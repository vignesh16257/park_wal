"""


# ##############two list in to dictionary

list=[1,2,3,4,5]
list_1=["sugan","balu","madhan","mano","jagan"]

list_new=dict(zip(list,list_1))

# print(list_new)

list_new_1={list[i] : list_1[i] for i in range(len(list))}

# print(list_new_1)
new_dict={}

for k in list:
    for v in list_1:
        new_dict[k]=v
        list_1.remove(v)

# print(new_dict)

list=[1,2,3,4,5]
list_1=["sugan","balu","madhan","mano","jagan"]
list_3={k:v for k,v in zip(list,list_1)}

print(list_3)



list_3=["anbu","balu","kadhir","gugan"]
list_2=[1,2,3,4]

dic = {k:v for k,v in zip(list, list_1)}

print(dic)


latest={}
for i in range(len(list_3)):
    latest[list_3[i]]=list_2[i]

print(latest)

"""




"""split one list in to two list"""

list=[2,4,5,6,6,7,8,9]

# method_1
list_first=list[:len(list)//2]
list_second=list[len(list)//2:]

# print(list_first)
# print(list_second)

#method_2

def halved_list(list):
    list_first = list[:len(list) // 2]
    list_second = list[len(list) // 2:]

    return print(list_first ,"\n", list_second)

################ halved_list(list)

#method_3
def split_List(list_1):

    mid=len(list)//2

    return list_1[:mid],list_1[mid:]

list_2,list_3=split_List(list)

# print(list_2,"\n",list_3)


#################Unpacking a list / tuple of pairs into two lists / tuples

source_list = [('1','a'),('2','b'),('3','c'),('4','d')]
# list1, list2 = zip(*source_list)

# print(list1,list2)

source_list_1 = [('1','a'),('2','b'),('3','c'),('4','d')]

list1 = [i[0] for i in source_list_1]
list2 = [i[1] for i in source_list_1]

print(list1,list2)


################Splitting a long tuple into smaller tuples