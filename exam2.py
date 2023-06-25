N=int(input())
result = ''
while N > 0:
    
    index = (N-1) % 26
    letter = chr(index + ord('A'))
    print(letter)
    result = letter + result
    N = (N-1) // 26
    
print(result)