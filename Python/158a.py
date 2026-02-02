def NextRound(k, sq):
    mile = sq[k-1]
    countPlayers = 0
    for s in sq:
        if s >= mile and s > 0 :
            countPlayers +=1
        
        if s < mile:
            break
    return countPlayers

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    ar = list(map(int,input().rstrip().split()))
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    print(NextRound(k,ar))