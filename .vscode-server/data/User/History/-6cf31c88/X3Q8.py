import random
import time

for num in range(1):
    num1 = random.randint(2,10)
    num2 = random.randint(5,10)
    num3 = random.randint(2,10)
    num4 = random.randint(2,8)
    
    num5 = random.randint(2,19)

    a = str(num1)
    b = str(num2)
    c = str(num3)
    d = str(num4)
    d1 = str(num4-1)
    d10 = int(num4-1)
    d2 = str(num4+1)
    d20 = int(num4+1)
    e = str(num5)

if c == e:
    d1 > b
    print("ERROR : Re-Run the code please")
else:
    command = ("Of two numbers "+a+" times the smaller one is less than "+b+" times the larger one by "+c+" If the sum of the number is larger than "+d+" times their diffrence by "+e+" find the two numbers")
    print(command)
    time.sleep(1)

    command1 = ("Then "+b+"x - "+a+"y = "+c+"...(i)")
    print(command1)
    time.sleep(1)

    command2 = ("(x + y) - "+d+" (x - y) = "+e)
    print(command2)
    time.sleep(1)

    sum = (" x + y - "+d+"x + "+d+"y = "+e)
    print(sum)
    time.sleep(1)

    sum1 = ("-"+d1+"x + "+d2+"y = "+e+"...(ii)")
    print(sum1)
    time.sleep(1)

    sum2 = num2*d20-d10*num1
    sum3 = num3*d20-num5*num1
    sum4 = sum3/sum2
    x = str(sum4)
if sum4 < 0:
    sum4*(+1)
    command3 = ("By solving (i) & (ii) we get x = "+x)
    print(command3)
    time.sleep(1)
else:
    command3 = ("By solving (i) & (ii) we get x = "+x)
    ab = command3
    format(command3,".2f")
    print(command3)
    









