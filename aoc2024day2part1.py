


with open("input2.txt", "r") as file:
    lines = file.readlines()

reports = []
for line in lines:

    reports.append( line.split())

totalUnsafe = 0
totalSafe=0



for report in reports:
    increasing = False
    decreasing = False


    if(int(report[1])-int(report[0])>0 and int(report[1])-int(report[0])<=3):
        increasing =True
    elif(int(report[1])-int(report[0])<0 and int(report[1])-int(report[0])>=-3):
        decreasing = True
    else:
        totalUnsafe +=1
        continue
    for i in range(1,len(report)):
        #increasing or decreasing
        diff =  int(report[i])-int(report[i-1])
        if abs(diff)>3:
            totalUnsafe += 1
            break
        elif(increasing and diff<0):
            totalUnsafe += 1
            break
        elif(decreasing and diff>0):
            totalUnsafe += 1
            break
        elif(diff==0):
            totalUnsafe += 1
            break

print(len(reports)-totalUnsafe)


