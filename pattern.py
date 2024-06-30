for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()
    
    
for i in range(6,1,-1):
    for j in range(1,i+1):
        print('*',end='')
    print()
    
    
print("------------------------------------------------------------------")

for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
    
print("------------------------------------------------------------------")

for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()
    
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()
    
print("------------------------------------------------------------------")
