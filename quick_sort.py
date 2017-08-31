from random import randint

def partition(v, begin, end):
    
    pivot = begin
    for i in range(begin + 1, end + 1):
        if v[i] <= v[begin]:
            pivot += 1
            v[i], v[pivot] = v[pivot], v[i]
            
    v[pivot], v[begin] = v[begin], v[pivot]
    return pivot

def quick_sort(v, begin, end):
    
    if end > begin:
        pivot = partition(v, begin, end)
        
        quick_sort(v, begin, pivot - 1)
        quick_sort(v, pivot + 1, end)
        
v = [randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9)]
print(v)
quick_sort(v, 0, len(v) - 1)
print(v)