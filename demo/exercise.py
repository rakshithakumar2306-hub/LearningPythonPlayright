"""for i in range(1, 11):
   print(i, end=" ")

for i in range(1,21):
    if i%2==0:
        print(i, end=" ")


for i in range(1,21):
    if i%2!=0:
        print(i, end=" ")

for i in range(1,51):
    i= i*(i+1)/2
    print(i, end=" ")

n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
"""

"""
for i in range(1,51):
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")
"""
#for i in range(1,101):
    #if i % 3 == 0 and i % 7== 0:
        #print(i)

"""
even =0
odd= 0
for i in range(1,101):
    if i %2 == 0:
      even = even + 1
    else:
       odd = odd + 1
print("even count:",even)
print("odd count:",odd)
"""
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))

if n1>n2 and n1>n3:
 print(n1, "is greater")
elif n2>n1 and n2>n3:
 print(n2, "is greater")
else:
  print(n3, "is greater")
