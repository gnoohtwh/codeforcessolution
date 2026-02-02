import math
def DominoPilling(m,n):
    s = m* n
    return math.floor(s/2)
    


if __name__ == '__main__':
    seriesinput = list(map(int,input().rstrip().split()))
    m = seriesinput[0]
    n = seriesinput[1]
    # square of board divided by square of default domino
    print(DominoPilling(m,n))
    