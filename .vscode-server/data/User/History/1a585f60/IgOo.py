num1 = int(input("Enter the 1st num : "))
num2 = int(input("Enter the 2nd num : "))
for n2 in range(num1,num2 + 1):
   if n2 > 1:
       for i in range(2,n2):
           if (n2 % i) == 0:
               break
       else:
           print(n2)
           
n1 = n2
n1 = int(n1)
res = sum(range(1, n1+1))
print("SUM of first ", n1, "numbers is: ", res)