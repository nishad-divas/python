r=int(input('enter the r number:'))
for i in range(1,r+1):
    for j in range(i):
        print('*',end='')
    print()
for i in range(r-1,0,-1):
  for j in range(i):
     print('*',end='')
  print()
