from random import randint

def merge(v, first, mid, last):
    l = v[first:mid]
    r = v[mid:last+1]
    l.append(float("inf"))
    r.append(float("inf"))
    
    i = j = 0
    for k in range(first, last + 1):
        if l[i] <= r[j]:
            v[k] = l[i]
            i += 1
        else:
            v[k] = r[j]
            j += 1
            
def merge_sort(v, first, last):
    if first < last:
        mid = (first + last)//2
        merge_sort(v, first, mid)
        merge_sort(v, mid + 1, last)
        merge(v, first, mid + 1, last)
    
v = [randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9)]
print(v)
merge_sort(v, 0, len(v)-1)
print(v)