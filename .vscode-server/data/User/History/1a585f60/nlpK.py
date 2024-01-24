num1 = int(input("Enter the 1st num : "))
num2 = int(input("Enter the 2nd num : "))
for n in range(num1,num2 + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
           
n1 = n
n1 = int(n1)
res = sum(range(1, n1+1))
print("SUM of first ", n1, "numbers is: ", res)