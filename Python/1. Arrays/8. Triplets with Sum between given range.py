A = input()
arr = [float(i) for i in A.split()]

less_than_1  = 0
less_than_2  = 0

for i in arr:
    if i<1/3:
        less_than_1+=1
    
    if i<2/3:
        less_than_2+=1

print(less_than_1,less_than_2)
no_in_goldilock = less_than_2-less_than_1

print("1") if no_in_goldilock>=3 else print("0") 
