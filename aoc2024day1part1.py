
list1=[]
list2=[]


with open("input1.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    split_text = line.split()
    list1.append(int(split_text[0]))
    list2.append(int(split_text[1]))

list1.sort()
list2.sort()

total=0

for n, k in zip(list1,list2):
    total += (k-n)

other=0

for i in range(len(list1)):
    other+= abs(list2[i]-list1[i])
#print(total)
#print(other)