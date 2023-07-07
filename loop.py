#write a program to print "hello" five times in the screen
a=1
while a<=5:
    print ("hello")
    a+=1
  
#write a program to print N natural numbers 
x= int(input("first natural numbers"))
y=1
while y<=x:
    print(y, end=" ")
    y=y+1


#write a program to print sum of N natural numbers 
x= int(input("first natural numbers"))
y=1
sum=0

while y<=x:
    sum=sum+y
    y=y+1
print(sum)  

#write a program to check whether a given number is prime or not  

x= int(input("enter number")) 
i=2
while i<=x-1:
    if x%i==0:
     break
    i=i+1
if i==x:
        print("number is prime")
else:
        print("not prime")

#write a program to print unicode of each character of string 
x="Telusko"
for y in x:
     print(y,"-", ord(y))






