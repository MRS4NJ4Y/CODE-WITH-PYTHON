#1. string numeric value can operate together with * (repeat)
a,b=2,3
txt = "@"
print (a*txt*b)

#2. string and straing can operate with + (concatenation)
a,b=2,3
txt = "@"
print((a*txt)*b)

#3. numeric value can operate together with all comparison operations
a,b=2,3
print (a==b)
print (a!=b)
print (a<b)
print (a<=b)

#4. numeric value can operate together with all arithmetic operations
a,b=2,3
c=4
print (a+b*c)

#5. arthmetic expression with integer and float will result in float
a,b=10,5.0
c=a*b
print(c)

#6. result of division operator with float integer will be float
a,b=1,2
c=a/b
print (c)

#7. integer division with float and int will give int displayed as float
a,b=1.5,3
c=a//b
print(c, a/b)

#8. floor gives closest integer wich is lesser then or equal to the float value result of (a//b) is same is floor (a/b)
a,b=12,5
c=a//b
print(c)

a,b=-12,5
c=a//b
print(c)

a,b=12,-5
c=a//b
print(c)

#9. remainder is negative when denominator is negative

a,b=-5,2
c=a%b
print(c)

a,b=-5,2
c=a%b
print(c)

a,b=5,-2
c=a%b
print(c)