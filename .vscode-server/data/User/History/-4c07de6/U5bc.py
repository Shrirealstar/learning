LI = int(input("Enter labour input : "))
MI = int(input("Enter Material Input : "))
CI = int(input("Enter Capital input : "))
EI = int(input("Enter energy input : "))
OM = int(input("Enter MISC input : "))
output = LI+MI+CI+EI+OM+500

print("Partial Productivity Measures are ")

LP = output/LI
print("Labour productivity is : ",LP)