def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_Apples = 0
    count_Oranges= 0

    for i in range(len(apples)):
        if a+apples[i] >= s and a+apples[i] <= t:
            count_Apples +=1
    for i in range(len(oranges)):
        if b+oranges[i] >= s and b+oranges[i] <=t:
            count_Oranges +=1
    print(f'Qirmizi zolaga dusen almalarin sayi: {count_Apples}')
    print(f'Qirmizi zolaga dusen portagallrin sayi sayi: {count_Oranges}')


st = input("Qirmizi zolagin baslangicini ve sonunu teyin edin: ").split()

s = int(st[0])

t = int(st[1])

ab = input("Alma ve portagal agaclarinin yerlesdiyi noqteleri teyin edin: ").split()

a = int(ab[0])

b = int(ab[1])

mn = input("Yere dusen alma ve portagallarin sayini teyin edin: ").split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input("Almalarin dusduyu noqteleri teyin edin: ").rstrip().split()))

oranges = list(map(int, input("Portagallarin dusduyu noqteleri teyin edin: ").rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)