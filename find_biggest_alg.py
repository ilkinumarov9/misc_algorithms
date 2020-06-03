
# This program produces maximum possible output in case of replacing
# one of the big number's digit with small number

nm1 = int(input("Enter big number(Only 4 digit): "))
nm2 = str(input("Enter small number: "))

# Getting digits from big number and converting them into strings
d1 = str(int(nm1/1000))
d2 = str(int((nm1%1000)/100))
d3 = str(int((nm1%100)/10))
d4 = str(int(nm1%10))

# Constructing 4 possible outputs after replacement
s1 = int(d1+d2+d3+nm2)
s2 = int(d1+d2+nm2+d4)
s3 = int(d1+nm2+d3+d4)
s4 = int(nm2+d2+d3+d4)

# Concatinating strings into a list and getting biggest number with max function
ls = [s1,s2,s3,s4]
bign = max(ls)

# Printing the output
print("Biggest possible number is ", bign)
