n, q = map(int, input().split())
l = [[] for _ in range(n)]

latsans = 0
for _ in range(q):
    a, x, y = map(int, input().split())
    if a == 1:
        l[(x^latsans)%n].append(y)
    else:
        t = (x^latsans)%n
        latsans = l[t][y%len(l[t])]
        print(latsans)
    #print(a, x, y, l)
