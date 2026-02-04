def BoyorGirl(s):
    count = 0 
    res = set()
    for i in range(len(s)):
        if s[i] not in res:
            res.add(s[i])
            count += 1
    
    return "CHAT WITH HER !" if count % 2 == 0 else "IGNORE HIM !"
if __name__ == '__main__':
    s= input()
    print(BoyorGirl(s))