import re
n = input("Enter a date : ")
if(re.findall(r'\d\d\d\d-\d\d-\d\d',n)):
    m =[ n[-2],n[-1],"-",n[-5],n[-4],"-",n[0],n[1],n[2],n[3]]
    print("".join(m))