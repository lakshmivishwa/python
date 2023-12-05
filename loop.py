# #write a program to print "hello" five times in the screen
# a=1
# while a<=5:
#     print ("hello")
#     a+=1
  
# #write a program to print N natural numbers 
# x= int(input("first natural numbers"))
# y=1
# while y<=x:
#     print(y, end=" ")
#     y=y+1


# #write a program to print sum of N natural numbers 
# x= int(input("first natural numbers"))
# y=1
# sum=0

# while y<=x:
#     sum=sum+y
#     y=y+1
# print(sum)  

# #write a program to check whether a given number is prime or not  

# x= int(input("enter number")) 
# i=2
# while i<=x-1:
#     if x%i==0:
#      break
#     i=i+1
# if i==x:
#         print("number is prime")
# else:
#         print("not prime")

# #write a program to print unicode of each character of string 
# x="Telusko"
# for y in x:
#      print(y,"-", ord(y))


# #write program to print first 10 odd natural numbers
# for i in range(1,11):
#      print(2*i-1)
     
# #write programto print square of first 4  numbers
# # i=4
# for i in range(1,5):
#      print(i**2 )

# #write program to print LCM of 2 numbers.
# i=4
# j=6
# l= i if i>j else j
# while l<=i*j:
#     if l%i==0 and l%j==0:
#           print ("LCM is", l)
#           break
#     l=l+1       
# print()

l1=[1,5,8,6,9,7,2]
print(sorted(l1))





