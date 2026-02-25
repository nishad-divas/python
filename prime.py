lover=int(input('enter lover limit :'))
upper=int(input('enter the upper limit :'))
for i in range(lover , upper+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        