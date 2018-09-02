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

wc={}
for line in data:
    words=line.split(' ')
    for word in words:
        if word in wc:
           wc[word]+=1
        else:
           wc[word]=1
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word]) 


while True:
    words=input('要查詢什麼字')
    if words == 'q':
        break
    if words in wc:
        print(words,'出現',wc[words],'次')
        continue
   
    else:
        print(words,'沒出現')
print('感謝使用本查詢功能')


    



















# average = total / len(data)
# print('平均資料長度',average)

# # 以下四行可寫成 new = [d for d in data if len(d) < 100]
# new=[]
# for d in data:
#     if len(d) < 100:
#       new.append(d)
# print('共有',len(new),'筆資料長度小於100')
# print(new[0])

# good=[]
# for d in data:
#     if 'good' in d:
#       good.append(d)
# print('共有',len(good),'含有good')
# print(good[0])