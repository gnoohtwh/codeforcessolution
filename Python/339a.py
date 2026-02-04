def HelpfulMath(s):
    res = dict()
    for c in s:
        if c != '+':
            res[c] = 1 + res.get(c,0)
    res = dict(sorted(res.items()))
    count = 0
    for k,v in res.items():
        for _ in range(v):
            print(k,end="")
            count += 1
            if count < len(s):
                print('+',end="")
                count +=1 
    

if __name__ == '__main__':
    s = input()
    HelpfulMath(s)
    
    