from random import randint

def selection_sort(v):
    j = 0
    while j < len(v):
        aux = j
        for i in range(j + 1, len(v), 1):            
            if v[i] < v[aux]:
                aux = i
        v[j], v[aux] = v[aux], v[j]
        j += 1        
        
v = [randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9)]
print(v) 
selection_sort(v)
print(v)       