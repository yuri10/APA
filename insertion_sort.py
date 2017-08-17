from random import randint

def insertion_sort(v):
    for i in range(1,len(v),1):
        for j in range(i,0,-1):
            if v[j] < v[j-1]:
                v[j], v[j-1] = v[j-1], v[j]
                               
v = [randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9)]
print(v) 
insertion_sort(v)
print(v)        



