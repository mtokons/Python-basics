mylist=[]
n=int(input("Enter size of the list:\n"))

for i in range(0,n):
    temp=int(input("Enter number to append:\n"))
    mylist.append(temp)

res = (sum(mylist))

print (res)