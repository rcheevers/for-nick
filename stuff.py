def main(n):
    return helper(n,[],0)

def helper(n, lis, g):
    if (g==n*n or len(lis)==2*n):
        return colinear(n,lis)
    temp = helper(n,lis+[g],g+1)
    temp2 = helper(n,lis,g+1)
    if (temp == 2*n or temp2 == 2*n):
        return 2*n
    return max(temp,temp2)

def colinear(n,lis):
    if(len(lis)<3):
        return len(lis)
    temp = colinear(n,lis[1:])
    if(temp==0):
        return 0
    slopes = []
    x1 = lis[0]
    for x2 in lis[1:]:
        rise = (x1//n-x2//n)
        run = (x1%n-x2%n)
        gcdResult = gcd(abs(rise),abs(run))
        slope = (rise/gcdResult,run/gcdResult)
        if slope in slopes:
            return 0
        slopes += [slope]
    return 1+temp

def gcd(a,b):
    if b>a:
        return gcd(b,a)
    if b==0:
        if a==0:
            return 1
        return a
    return gcd(b,a%b)

def show(n,lis):
    mat = []
    for x in range(n):
        mat += [[]]
        for y in range(n):
            mat[x] += [0]
    for x in lis:
        mat[x//n][x%n]=1
    for x in mat:
        print(x)
    print("")
