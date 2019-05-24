with open("log_files/201811113009.log", encoding='utf8') as filepointer:
    count=0
    for line in filepointer :
        line1 = line.split(',')[1]
        line2 = line1.split('：')[1]
        if  line2=='201811113009' :
            count = count+1
print(count)
