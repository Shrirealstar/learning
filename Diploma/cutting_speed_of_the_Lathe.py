from cmath import pi


d=float(input("Enter the dia of the job :"))
l=float(input("Enter the leangth of the job :"))
f=float(input("Enter the feed :"))
n=float(input("Enter RPM :"))
#Speed of cut
S=pi*d*(n/1000)
print('Speed in RPM is :',S)

#Time Taken to cut the job
T=l/n*f
print('Time taken to cut in min is :',T)