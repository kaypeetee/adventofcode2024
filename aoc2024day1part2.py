
with open("input1.txt", "r") as file:
    lines = file.readlines()
list1=[]
list2=[]
for line in lines:
    split_text = line.split()
    list1.append(int(split_text[0]))
    list2.append(int(split_text[1]))

freq2 = [0]*(max(list1)+1)

for num in list2:
    freq2[num] +=1


similarityscore=0

for number in list1:
    calculation  = number*freq2[number]

    similarityscore+= calculation


print(similarityscore)