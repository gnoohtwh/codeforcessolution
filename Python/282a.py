

def Bit(s):
    cSet = set()
    for c in s:
        cSet.add(c)
    if '+' in cSet and 'X' in cSet:
        return True
    elif '+' in cSet and 'X' in cSet:
        return False
res = 0    
n = int(input())
for i in range(n):
    s = input()
    if Bit(s):
        res += 1
    else:
        res -= 1
print(res)