n=float(input("enter float number:"))
integer_part=int(n)
fraction_part=n-integer_part
#interger part
b= bin(integer_part)[2:]
binary_frac=""
#fraction part
while fraction_part!=0:
    fraction_part*=2
    bit=int(fraction_part)
    binary_frac=str(bit)+binary_frac
    fraction_part-=bit
f=fraction_part
print("binary=",b + "." + binary_frac)