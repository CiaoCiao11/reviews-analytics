data=[]
count=0
total=0
with open ('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        total += len(line)
        count += 1
        if count% 1000 == 0:
        	print(len(data))
       
print('檔案讀完了，共有',len(data),'筆資料')
average = total / len(data)
print('平均資料長度',average)

new=[]
for d in data:
    if len(d) < 100:
      new.append(d)
print('共有',len(new),'筆資料長度小於100')
print(new[0])

good=[]
for d in data:
    if 'good' in d:
      good.append(d)
print('共有',len(good),'含有good')
print(good[0])