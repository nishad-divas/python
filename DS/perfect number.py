def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i

    if sum==n:
        print(n, "is a prefect number")
    else:
          print(n, 'is not a prefect  number')
n=int(input('enter a number: '))
perfect_number(n)