def plusMinus(arr):
    x,z,y=0,0,0
    for i in range(0,len(arr)):
        if arr[i]>0:
            x = x + 1
        elif arr[i]<0:
            y = y + 1
        else:
            z = z + 1
    print(float(x/len(arr)))
    print(float(y/len(arr)))
    print(float(z/len(arr)))
    
plusMinus([1,-2,0,3,4,-9])