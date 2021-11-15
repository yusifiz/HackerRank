def gradingStudents(grades):

    for i in range(len(grades)):
        if grades[i] >= 38:
            nxt_num = (grades[i] - (grades[i] % 5))+5
            deff = nxt_num - grades[i]

            if deff < 3:
                grades[i] = nxt_num

    return grades

print(gradingStudents([37,78,98,13,57]))