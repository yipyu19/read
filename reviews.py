data = []
count = 0
with open('111.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))
print('檔案讀取完了，總共有',len(data),'筆資料')
# print(len(data))
# print(data[0])
# print('-----------------------------------')
# print(data[1])

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('每筆的平均長度爲',sum_len/len(data))

# if len(data) < 100:
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有',len(new),'筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
printprint('一共有',len(good),'筆留言有good字眼')

