a=input("１番目の数字を入力してください")
b=input("演算子を入力してください")
c=input("2番目の数字を入力してください")

if b=="+":
    print("足し算ですね。答えは",float(a)+float(c)) 

if b=="-":
    print("引き算ですね。答えは", float(a)-float(c))

if b=="*":
    print("掛け算ですね答えは",float(a)*float(c)) 

if b=="/":
    print("割り算ですね。答えは",float(a)/float(c)) 