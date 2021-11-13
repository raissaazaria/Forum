file =open("myVacation.txt","r")
myList = file.readlines()

count= 0
for line in myList:
    count= count + 1
    print(count,".", line,sep="",end="")