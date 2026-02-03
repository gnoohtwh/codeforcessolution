# Beautiful Matrix

def FindIndex(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                return [i,j]
    pass

def BeautiMat(matrix): #Checking if the location has the nearest index to the third column or row
    oneNumLocation = FindIndex(matrix)
    i = oneNumLocation[0]
    j = oneNumLocation[1]
    count = 0
# i = 1, j = 4
    while True:
        if abs(i - 2) >= abs(j - 2) and i != 2 :
            if i < 2:
                i += 1
                count += 1
            elif i > 2:
                i -= 1
                count += 1
        elif abs(i - 2) < abs(j - 2) and j != 2 :
            if j < 2:
                j += 1
                count += 1
            elif j> 2:
                j -= 1
                count += 1



        if i == 2 and j == 2:
            return count
            break

    

if __name__ == '__main__':
    arr = []
    for _ in range(5):
        l = list(map(int,input().rstrip().split()))
        arr.append(l)
    print(BeautiMat(arr))
    # matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]
    # print(FindIndex(matrix))
    # print(BeautiMat(matrix))