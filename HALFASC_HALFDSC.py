l=list(map(int,input().split()))
l.sort()
k=len(l)//2
for i in range(len(l)//2):
    print(l[i],end=" ")
for j in range(len(l)-1,len(l)//2-1,-1):
    print(l[j],end=" ")
