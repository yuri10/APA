from random import randint

def swap(i, j):                    
    v[i], v[j] = v[j], v[i] 

def heapify(end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and v[i] < v[l]:   
        max = l   
    if r < end and v[max] < v[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def heap_sort(v):     
    end = len(v)   
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)   

v = [randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9)]
print(v)
heap_sort(v)
print(v)