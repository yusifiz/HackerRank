def sequential(s,sub_string):
    if not s: return True
    if s.startswith(sub_string):
        l = len(sub_string)
        return sequential(s[l:],str(int(sub_string)+1))
    return False
    
def separateNumbers(s):
    for i in range(1,len(s)//2+1):
        sub_string = s[:i]
        if sequential(s,sub_string):
            return "YES "+sub_string
    return "NO"

for _ in range(int(input())):
    s = input()
    print(separateNumbers(s))