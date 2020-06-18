"""
dictionaryのinはキーのみを参照
19：41
format文を使って

"""
word ="すもももももももものうち\n"
count_dict={}
for char in word:
    if char not in count_dict:
        count_dict[char]=1
    else:
        count_dict[char]+=1
print(count_dict)   

for key,value in count_dict.items():
    print("「{}」の個数は{}個です。".format(key,value))