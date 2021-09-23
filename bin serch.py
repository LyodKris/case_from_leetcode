a = [1,3,4,5,7,10,13,35,46,57]
value = 50
mid = len(a) // 2
low = 0
high = len(a) - 1
 
while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
 
if low > high:
    print(low)
else:
    print("ID =", mid)