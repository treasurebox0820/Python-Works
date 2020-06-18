"""

"""
from pywork_4_1_2 import BMI
import random

if __name__ == "__main__":
    random.seed(42)
    with open("sample4.txt","w") as f:
        for i in range(1,10001):
            you = BMI()
            you.weight = random.randrange(20,101)
            you.height = random.randrange(100,230)
            you.bmi = you.cal_bmi(you.height,you.weight)
            you.id = i
            you.body_is = you.judge_bmi(you.bmi)
            f.write(f"{you.id}, {you.weight}, {you.height}, {you.body_is}\n")
    

    weight_max = 0
    weight_min = 1000
    height_max = 0
    height_min = 1000
    total_weight = 0
    total_height = 0
    with open("sample4.txt","r") as f:
        for i in f :
            one_list = i.split(",")
            
            weight_1 = int(one_list[1])
            height_1 = int(one_list[2])
            if weight_1 > weight_max:
                weight_max = weight_1
            if weight_1 < weight_min:
                weight_min = weight_1
            if height_1 > height_max:
                height_max = height_1
            if height_1 < height_min:
                height_min = height_1
            total_weight += int(one_list[1])
            total_height += int(one_list[2])


print(f"身長の最大値は{height_max},最小値は{height_min}\n体重の最大値は{weight_max},最小値は{weight_min}")
print(f"平均体重は{total_weight/10000},平均身長は{total_height/10000}")