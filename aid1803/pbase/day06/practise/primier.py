n = 1000
primier= []
result = []
L=[True]*(n+1)
for i in range(2,int(n**(1/2))):
    if L[i] == True:
        for j in range(2,i):
            if i % j == 0:
                L[i] == False    
        else:
            for k in range(2,int(n/i)+1):
                L[k*i] = False
for a in range(2,n+1):
    if L[a]== True:
        primier.append(a)

for c in range(len(primier)):
    b = primier[c]
    print('%.1f%%'%(c/len(primier)*100))
    
    if 2**b-1 in primier:
        result.append((2**b-1)*2**(b-1)) 

print (result)