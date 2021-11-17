def closestNumbers(arr):
    arr.sort()
    min_dif = abs(arr[0]-arr[1])
    l1st = []
    for i in range(len(arr)-1):
        d = abs(arr[i]-arr[i+1])
        if d==min_dif:
            l1st += [arr[i], arr[i+1]]
            min_dif =d
        elif d<min_dif:
            l1st = [arr[i], arr[i+1]]
            min_dif =d
    return l1st

print(closestNumbers([3,6,8,-3,7,90,21,-4,5,0]))