#given two numberz 
#ITS ARRAYYYY FJDJFDJKLAFJAKDJFLK
N=int(input())
s=int(input())
digits = [0*N]
    
for i in range(N):
    if s >= 9:
        digits[i] = 9
        s=s-9
    else:
        digits[i] = s
       
print(int("".join(map(str, digits))))