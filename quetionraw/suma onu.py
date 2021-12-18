
"""
list=[1,2,3,4,5]
list_1=["sugan","balu","madhan","mano","jagan"]

latest = {}
for i in range(len(list)):
    latest[list[i]]=list_1[i]

# print(latest)

new_list={list[i]:list_1[i] for i in range(len(list))}

# print(new_list)

f={}

for k in list:
    for v in list_1:
        f[k]=v
        list_1.remove(v)

print(f)

"""



t = (2, 2, 10, 10, 344, 344, 45, 43, 2, 2, 10, 10, 12, 8, 2, 10)


parts = (t[0:4], t[4:8], t[8:12], t[12:16])
# print(parts)

# or as a function
def grouper2(t,n):

    return [t[i:i + n] for i in range(0, len(t), n)]

# print(grouper2(t,4))




# return [t[i:i + n] for i in range(0, len(t), n)]


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "Geeksforgeeks"

print(reverse(s))















