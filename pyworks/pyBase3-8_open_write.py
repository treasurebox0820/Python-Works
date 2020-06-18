with open("sample.txt","w",encoding="utf-8") as f:
    f.write("test")
#読み出し
f= open("sample.txt","r")
data=f.read()
print(data)
f.close()

with open("sample.txt","r") as f:
    data = f.read()
    print(data)