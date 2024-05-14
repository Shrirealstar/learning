n1 = list(input("Enter the binary list(Use only 1's and 0's) : "))

n1 = [int(x) for x in n1]

pary1 = 0
pary0 = 0

for x in n1:
    if x == 1:
        pary1 +=1
    elif x == 0:
        pary0 +=1

print("Number of 1's : ",pary1)
print("Number of 0's : ", pary0)

if pary1 % 2 ==0:
    pary1 = 0
else:
    pary1 = 1
n1 = n1 + [pary1]
print(n1)