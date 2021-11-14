def aVeryBigSum(ar):
    x=0
    for i in range(0,len(ar)):
        x= x + ar[i]
    return x

print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))