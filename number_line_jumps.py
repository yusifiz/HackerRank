# x1 - 1ci kenqurunun basladigi noqte
# x2 - 2ci kenqurunun basladigi noqte
# v1 - 1ci kenqurunun tullandigi mesafe
# v2 - 2ci kenqurunun tullandigi mesafe

def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return 'NO'
    else:
        if v1!=v2 and (x2-x1)%(v2-v1)==0:
            return 'YES' 
        else:
            return 'NO'
        
print(kangaroo(0,3,8,2))