def Team(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        
        if count == 2:
            return True
        
n = int(input())
res = 0
for i in range(n):
    ar = list(map(int, input().rstrip().split()))
    if Team(ar)== True:
        res += 1
    ar = []

print(res)