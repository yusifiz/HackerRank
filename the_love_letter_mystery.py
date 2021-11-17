for _ in range(int(input())):
    count=0
    word=input()
    for i in range(len(word)//2):
        if word[i]!=word[-i-1]:
            count+=abs(ord(word[i])-ord(word[-i-1]))
    print(count)

