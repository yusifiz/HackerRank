

def hackerrankInString(str):
    a = "hackerrank"
    b = 0
    for i in str:
        if i == a[b]:
            b+=1
        if b >= 10:
            break
    if b == 10:
        print("YES")
    else:
        print("NO")
    
hackerrankInString('hereiamstackerrank')
    