def sockMerchant(ar):
    pears = 0
    color = []
    for i in range(len(ar)):
        if ar[i] not in color:
            color.append(ar[i])
        else:
            pears += 1 
            color.remove(ar[i])
    return pears

print(sockMerchant([1,2,3,2,1,5,6,1]))