N=int(input())
M=list(map(int,input().split()))
print(M)
for i in M:
    for j in M:
        list=[(x,y) for x in i for y in j]
        print(list)
    