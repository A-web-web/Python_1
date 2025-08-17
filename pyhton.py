a=[1,2,3,4,5,6,7,8,9]

x = 4

low = 0
high= len(a)-1
found = 0
index = -1

while low <= high:
    mid = (low + high)//2
    if a[mid] == x:
        found = 1
        index =  mid
        break
    elif a[mid] < x:
       low=  mid+ 1
    else:
       high= mid- 1

if found:
 
    print("Element ",x, "found at index" ,index,".")
else:
    print(f"Element {x} not found in the list.")
