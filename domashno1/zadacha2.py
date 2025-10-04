grades = [95, 82, 67, 54, 100, 73, 88, 42]
Excellent = []
Good = []
Pass = []
Fail = []
for grade in grades:
    if grade>=90:
     Excellent.append(grade)
    
    if 70<=grade<=89:
     Good.append(grade)
    
    if 50<=grade<=69:
     Pass.append(grade)
    
    if grade<50:
     Fail.append(grade)
print(Excellent)
print(Good)
print(Pass)
print(Fail)