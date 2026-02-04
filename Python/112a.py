# Petya and Strings

def PeytaPresent(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()

    m1,m2 = 0,0
    for i in range(len(s1)):
        if ord(s1[i]) != ord(s2[i]):
            if ord(s1[i]) <ord(s2[i]): 
                return -1
            elif ord(s1[i]) > ord(s2[i]):
                return 1
    return 0
if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(PeytaPresent(s1,s2))
