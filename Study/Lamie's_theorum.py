import math

T1=int(input("Enter T1 : "))
T2=int(input("Enter T2 : "))
T3=int(input("Enter T3 : "))

sin1=int(input("Enter sin1 : "))
sin2=int(input("Enter sin2 : "))
sin3=int(input("Enter sin3 : "))


#T3 is given and wanted to find out T1
n=T3*math.sin(math.radians(sin1))/math.sin(math.radians(sin3))

print('If T3 given, then the Value of T1 is :',n)

#T3 is given and wanted to find out T2
n3=T3*math.sin(math.radians(sin2))/math.sin(math.radians(sin3))

print('If T3 given, then the Value of T2 is :',n3)

#T2 is given and wanted to find out T3
n4=T2*math.sin(math.radians(sin3))/math.sin(math.radians(sin2))

print('If T2 given, then the Value of T3 is :',n4)
#T2 is given and wanted to find out T1
n1=T2*math.sin(math.radians(sin1))/math.sin(math.radians(sin2))

print('If T2 given, then the Value of T1 is :',n1)

#T1 is given and wanted to find out T3
n5=T1*math.sin(math.radians(sin3))/math.sin(math.radians(sin1))

print('If T1 given, then the Value of T3 is :',n5)

#T1 is given and wanted to find out T2
n2=T1*math.sin(math.radians(sin2))/math.sin(math.radians(sin1))

print('If T1 given, then the Value of T2 is :',n2)







