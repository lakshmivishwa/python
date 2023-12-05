# x="abc"
# y= int(x) #getting error, it is valueError, We can't convert alpha string into int

# a="88"
# b= int(a)
# print(b)

# c= "1.8"
# d= int(c)
# print(d) #error first we need to convert in int

c= "1.8"
d= float(c) #first we need to convert in float
e= int(d)
print(e)