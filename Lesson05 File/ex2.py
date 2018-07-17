import csv
with open('AQI.csv','r', encoding='utf-8-sig') as f:
    
    reader = csv.reader(f)
    k = []
    q = []
    ##建立兩個list 
    next(reader) ##略過reader的第一項
    for row in reader:           ##讀取reader裡面的 每一排
        k.append(int(row[2]))  
        q.append(row[0])
        ##在兩個list添加對應的項目
   
    AQI = k[k.index(min(k))]
    SiteName = q[k.index(min(k))]
    # 找出list K 裡面的最小值的index是幾
    # 對應list Q 裡面的相同位置

    print('{}空氣最好，AQI是{}'.format(SiteName,AQI))