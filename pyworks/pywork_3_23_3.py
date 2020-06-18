"""
1.while文を使って、1から30までの数字を表示し、数字が 3の倍数なら数字の横に Fizz、5の倍数なら Buzz、 
3 と 5 のいずれの倍数でもあるなら FizzBuzz と表示してください。
"""
"""
伊藤さん発表
while文のなかにfor文があったが
"""
i=1
while i<=51:
    if i%3==0 and i%5==0:
        print("FizzBuzz",end=",\n",)
    
    elif i%3==0:
        print("Fizz",end=",\n")
    elif i%5==0:
        print("Buzz",end=",\n")
    else:
        print(i,end=",  ")
    i+=1
