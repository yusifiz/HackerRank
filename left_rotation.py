def rotLeft(a, d):
    alist = list(a)
    rotated_list = alist[d:]+alist[:d]
    return rotated_list