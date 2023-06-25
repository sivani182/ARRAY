N=int(input())
s=int(input())
digits = [0]*N

    
for i in range(0,N):
    if s >= 9 :
        digits[i] = 9
        s=s-9
    elif(0<s<9) :
        digits[i] = s
        s=s-9
        
print(("%".join(map(str, digits))))