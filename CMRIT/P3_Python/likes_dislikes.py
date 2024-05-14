n1 = list(input("Enter the 1st person's list(Use only 1's and 0's) : "))
n2 = list(input("Enter the 2nd person's list(Use only 1's and 0's) : "))

n1 = [int(x) for x in n1]
n2 = [int(x) for x in n2]

like_p1 = 0
dislike_p1 = 0

like_p2 = 0
dislike_p2 = 0

for x in n1:
    if x == 1:
        like_p1 +=1
    elif x == 0:
        dislike_p1 +=1

for x in n2:
    if x == 1:
        like_p2 +=1
    elif x == 0:
        dislike_p2 +=1
print("Likes of 1st person : ",like_p1)
print("Dislikes of 1st person : ", dislike_p1)
print("Likes of 2nd person : ", like_p2)
print("Dislikes of 2nd person : ", dislike_p2)
