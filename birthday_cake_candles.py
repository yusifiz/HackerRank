def birthdayCakeCandles(ar):

    ar.sort()

    result = ar.count(ar[len(ar)-1])
    return result

print(birthdayCakeCandles([4,1,1,3,5,5]))