import sys

# for i in range(6):
#     print(i)


set = {1,2,3,8,39,103,7,29,49,9}


list = [1,39,0,30,20,40,192,503,5]

dist = {1:"Shubham",
        2:"Aman",
        3:"Chinmay",
        4:"Vivek"
        }


l = len(dist)

print(l)

for i in range(len(dist)):
    print(dist.get(i+1))


t =  (1,3,5,6,8,9,0)

for i in t:
    print(i)
print("----------------")
s = {1,2,2,3,3,4,5,5,6,3,2,2,6}

for j in s:
    print(j)