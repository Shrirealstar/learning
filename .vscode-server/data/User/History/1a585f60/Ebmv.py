num1 = int(input("Enter the 1st num : "))
num2 = int(input("Enter the 2nd num : "))
for n in range(num1,num2 + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               list.append (n)
               break
       else:
           print(n)
           