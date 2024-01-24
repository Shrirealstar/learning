# LCM of any Two Numbers
num1=int(input("Enter 1st Number :"))
num2=int(input("Enter 2nd Number :"))
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

x = num1
y = num2

print("The L.C.M. is", compute_lcm(num1, num2))